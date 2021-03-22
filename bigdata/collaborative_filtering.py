from surprise import Reader, Dataset
from surprise import KNNBasic
from surprise.model_selection import cross_validate, train_test_split
import pandas as pd
import shutil


if __name__ == "__main__":
    ratings = pd.read_csv("리뷰데이터크롤링.csv", encoding="cp949")
    # ratings = pd.read_csv("리뷰데이터크롤링(모두보기).csv", encoding="cp949")
    # print(ratings.loc[0])
    ratings.columns = ['review_id', 'book_id', 'nickname',
                       'score', 'sympathy', 'regtime', 'content']
    # ratings.columns = ['review_id', 'book_id', 'user_id', 'nickname',
    #                    'score', 'sympathy', 'regtime', 'content']
    ratings.drop(index=0, inplace=True)

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w
    print('[기존 ratings]')
    print(f"{separater}\n")
    print(ratings[:15])
    print(f"\n{separater}\n")

    # 유저가 남긴 최소 리뷰의 수 : 5개
    min_user_ratings = 5
    filter_users = ratings['nickname'].value_counts() >= min_user_ratings
    filter_users = filter_users[filter_users].index.tolist()

    ratings_new = ratings[ratings['nickname'].isin(filter_users)]
    print(f"{separater}\n")
    print('[갱신된 ratings]')
    print(ratings_new[:15])
    print(f"\n{separater}\n")

    print('기존 ratings shape : \t{}'.format(ratings.shape))
    print('갱신된 ratings shape : \t{}'.format(ratings_new.shape))

    print(f"\n{separater}\n")

    print('score min value : {}'.format(ratings['score'].min()))
    print('score max value : {}'.format(ratings['score'].max()))

    print(f"\n{separater}\n")

    reader = Reader(rating_scale=(1.0, 5.0))
    data = Dataset.load_from_df(
        ratings_new[['nickname', 'book_id', 'score']], reader)

    train, test = train_test_split(data, test_size=0.25, random_state=42)

    # KNN 알고리즘으로 객체 생성 후 학습 수행
    algo = KNNBasic()
    algo.fit(train)

    prediction = algo.test(test)
    print('prediction type: ', type(prediction), 'size: ', len(prediction))

    print(f"\n{separater}\n")

    # user id, item id, 예측평점값들만 추출해서 하나의 튜플에 담겨있게 하기
    result = [(pred.uid, pred.iid, pred.est) for pred in prediction[:5]]
    print(result)

    print(f"\n{separater}\n")

    # 개별 데이터에 대한 예측값 반환은 predict() 사용
    uid = '지니'
    iid = '56869333'
    pred = algo.predict(uid, iid)
    print(pred)

    print(f"\n{separater}\n")

    # RMSE방식 교차검증
    cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=True)
