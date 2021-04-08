import pymysql
import pandas as pd
import shutil
import random

term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w

def preprocessing(ratings, min_user_ratings=5, min_book_ratings=15):
    # 유저가 남긴 최소 리뷰의 수 : default 5개
    # 책에 있는 최소 리뷰의 수 : default 15개
    filter_books = ratings['book_isbn'].value_counts() >= min_book_ratings
    filter_books = filter_books[filter_books].index.tolist()
    ratings = ratings[ratings['book_isbn'].isin(filter_books)]

    filter_users = ratings['user_id'].value_counts() >= min_user_ratings
    filter_users = filter_users[filter_users].index.tolist()
    ratings_new = ratings.copy()[ratings['user_id'].isin(filter_users)]
    # 크롤링 데이터의 user_id 는 db에서 얻어온 사용자의 id와 겹치지 않게 '!'를 붙여줌
    ratings_new.loc[:,'user_id'] += '!'

    return ratings_new


def view_table(data, user_id):
    user_data = data[data['user_id'] == user_id]
    print(user_data)


if __name__ == "__main__":
    conn = pymysql.connect(host='j4a205.p.ssafy.io', user='root', db='readme', password='ssafy', charset='utf8')
    cursor = conn.cursor()
    ratings = pd.read_pickle('./data/리뷰데이터크롤링(모두보기).pkl')
    ratings.columns = ['book_id', 'book_isbn', 'user_id', 'nickname', 'score']
    ratings.drop(index=0, inplace=True)

    ratings_new = preprocessing(ratings, 5, 10)

    print('[전처리된 ratings]')
    print(f"{separater}\n")
    print(ratings_new[: 100])
    print(f"\n{separater}\n")


    users = ratings_new['user_id'].unique()
    user_list = list(users)
    user_list = user_list[0:30]
    print(user_list)

    # review_content[5][~] 
    review_content = [['너무 지루하고 재미없어요', '제 취향과는 안맞는 책', '읽는데 시간이 아깝다는 생각이 드는 책', '돈이 아까워요', '괜히 읽었다는 생각이 드는 책'],
    ['그닥.. 재미없어요', '2점이 적당하네요', '남에게 추천할만큼 재밌지는 않아요', '별로에요', '기대보다 재미없음',
    '지루하다. 몰입이 안됨', '지루하고 루즈해요'],
    ['그럭저럭', '좋지도 않고 나쁘지도 않아요', '그냥 시간떼우기 좋은 책이네요', '3점 정도 줄만한 책이에요', '볼만하네요',
    '너무 기대를 해서 그런지 약간 실망했어요', '살만한 책은 아닌듯. 빌려보세요'],
    ['재밌는 책이네요 ㅎㅎ', '기대하지 않았는데 생각보다 재밌네요', '많은 생각이 들게하는 책. 추천합니다', '신선한 책이네요. 좋아요', '잠깐 읽어봤는데 재밌네요',
    '한 문장 한 문장이 너무 재밌네요.', '추천받아 읽은 책. 재밌네요', '재미있어요'],
    ['제 삶을 바꾼 책입니다. 강추합니다!', '와 너무 좋습니다. 이 책만 기다렸어요.', '제 기대를 만족시킨 책입니다', '너무 설렙니다. 최고의 책이에요!', '가슴이 웅장해진다..', 
    '제 인생 책입니다. 너무 좋아요', '몰입도 있게 읽은 책입니다', '이 책을 읽고 많은 도움이 되었습니다.', '문장 하나하나가 너무 좋아요', '기다리고 기다리던 책. 제 기대를 만족시켜주네요']]
    print(review_content[0])
    user_id_idx = 0
    for user_id in user_list:
        user_id_idx += 1
        user_review_list = ratings_new[ratings_new['user_id'] == user_id]
        print(user_review_list)
        # print(type(user_review_list))
        for i, row in user_review_list.iterrows():
            # print(row)
            # print(type(row))
            score = row[4]
            length = len(review_content[score-1])
            r = random.randrange(0, length)
            content = review_content[score-1][r]
            book_isbn = row[1]
            sql = """INSERT INTO books_review
            (user_id, review_rating, review_content, review_date, book_isbn) 
            values (%s, %s, %s, now(), %s)
            """
            cursor.execute(sql, (user_id_idx, score, content, book_isbn))
    
    conn.commit()