from surprise import Reader, Dataset
from surprise import KNNBasic, KNNWithMeans, KNNBaseline, SVD, NMF
from surprise.model_selection import cross_validate, train_test_split
import pandas as pd
import shutil

term_w = shutil.get_terminal_size()[0] - 1
separater = "-" * term_w


def preprocessing(ratings, min_user_ratings=5, min_book_ratings=15):
    # 유저가 남긴 최소 리뷰의 수 : default 5개
    # 책에 있는 최소 리뷰의 수 : default 15개
    filter_books = ratings['book_id'].value_counts() >= min_book_ratings
    filter_books = filter_books[filter_books].index.tolist()
    ratings = ratings[ratings['book_id'].isin(filter_books)]

    filter_users = ratings['nickname'].value_counts() >= min_user_ratings
    filter_users = filter_users[filter_users].index.tolist()
    ratings_new = ratings[ratings['nickname'].isin(filter_users)]

    return ratings_new


def get_unread_book_list(ratings, books, user_id):
    # 특정 유저가 본 book_id들을 리스트로 할당
    read_books = ratings[ratings['nickname'] == user_id]['book_id'].tolist()
    unread_books = [book_id
                    for book_id in books if book_id not in read_books]

    return unread_books


def recommend(algo, user_id, unread_books, top_n=10):
    # predict()를 이용해 user_id의 평점이 없는 책들에 대해 평점 예측
    predictions = [algo.predict(user_id, book_id) for book_id in unread_books]

    # 리스트를 정렬하는 sort() 인자의 key값에 예측평점(est값)을 넣어줘야함.
    def sortkey_est(pred):
        return pred.est

    # 예측평점을 기준으로 내림차순 정렬
    predictions.sort(key=sortkey_est, reverse=True)
    # 상위 n개의 예측값들을 가져옴
    top_predictions = predictions[:top_n]

    top_book_predictions = [(pred.iid, pred.est) for pred in top_predictions]

    # # top_predictions에서 movie_id, 예측평점을 각각 뽑아내서 zip으로 묶음
    # top_book_ids = [pred.iid for pred in top_predictions]
    # top_book_ratings = [pred.est for pred in top_predictions]

    # # zip함수를 사용해서 리스트의 똑같은 위치에 있는 값들을 묶음
    # top_book_predictions = [(book_id, rating)
    #                         for book_id, rating in zip(top_book_ids, top_book_ratings)]

    return top_book_predictions


def algo_test(algos, data):
    results = []

    for algo in algos:
        # RMSE방식 교차검증
        result = cross_validate(algo, data, measures=[
                                'RMSE'], cv=5, verbose=False)

        # 결과저장
        verbose = pd.DataFrame.from_dict(result).mean(
            axis=0)   # rmse, 훈련시간, 테스트시간 평균값 저장
        verbose = verbose.append(
            pd.Series([str(algo).split(' ')[0].split('.')[-1]], index=['Algorithm']))
        results.append(verbose)

    return pd.DataFrame(results).set_index('Algorithm').sort_values('test_rmse')


def main():
    # ratings = pd.read_csv("리뷰데이터크롤링.csv", encoding="cp949")
    # ratings = pd.read_csv("리뷰데이터크롤링(모두보기).csv", encoding="cp949")
    ratings = pd.read_pickle('./data/리뷰데이터크롤링(모두보기).pkl')
    ratings.columns = ['book_id', 'user_id', 'nickname',
                       'score']
    ratings.drop(index=0, inplace=True)

    print('[기존 ratings]')
    print(f"{separater}\n")
    print(ratings[: 15])
    print(f"\n{separater}\n")

    ratings_new = preprocessing(ratings, 3)

    print('[전처리된 ratings]')
    print(f"{separater}\n")
    print(ratings_new[: 15])
    print(f"\n{separater}\n")

    print('기존 ratings shape : \t{}'.format(ratings.shape))
    print('전처리된 ratings shape : \t{}'.format(ratings_new.shape))

    print(f"\n{separater}\n")

    # print('score min value : {}'.format(ratings['score'].min()))
    # print('score max value : {}'.format(ratings['score'].max()))
    users = ratings['nickname'].unique()
    print("기존 유저의 수 : {user_cnt}\n".format(user_cnt=len(users)))
    books = ratings['book_id'].unique()  # 일단 unique한 값으로 book_id를 뽑음
    print("기존 책의 개수 : {book_size}\n".format(book_size=len(books)))

    print()
    users = ratings_new['nickname'].unique()
    print("유저의 수 : {user_cnt}\n".format(user_cnt=len(users)))
    books = ratings_new['book_id'].unique()  # 일단 unique한 값으로 book_id를 뽑음
    print("책의 개수 : {book_size}\n".format(book_size=len(books)))

    print(f"\n{separater}\n")

    reader = Reader(rating_scale=(1.0, 5.0))
    data = Dataset.load_from_df(
        ratings[['nickname', 'book_id', 'score']], reader)

    return data, ratings_new


def test(data):
    # 여러 개의 알고리즘 테스트
    algos = [KNNBasic(), KNNWithMeans(), KNNBaseline(), SVD(), NMF()]
    test_result = algo_test(algos, data)
    print(test_result)


def recomm(data, ratings, user_id):
    train, test = train_test_split(data, test_size=0.25)

    # 적절한 알고리즘으로 객체 생성 후 학습 수행
    algo = SVD()
    algo.fit(train)

    prediction = algo.test(test)
    print('prediction type: ', type(prediction), 'size: ', len(prediction))

    print(f"\n{separater}\n")

    # user id, item id, 예측평점값들만 추출해서 하나의 튜플에 담겨있게 하기
    result = [(pred.uid, pred.iid, pred.est) for pred in prediction[:5]]
    print(result)

    print(f"\n{separater}\n")

    # 개별 데이터에 대한 예측값 반환은 predict() 사용
    books = ratings['book_id'].unique()  # 일단 unique한 값으로 book_id를 뽑음
    unread_books = get_unread_book_list(ratings, books, user_id)
    top_n_pred = recommend(algo, user_id, unread_books)
    for i, top_book in enumerate(top_n_pred):
        print('{rank}위 : {book_id}(예측평점 : {book_est})'.format(
            rank=i + 1, book_id=top_book[0], book_est=top_book[1]))

    print(f"\n{separater}\n")


if __name__ == "__main__":
    data, ratings = main()
    # user_id = '지니'
    recomm(data, ratings, '미리내')
    # test(data)
