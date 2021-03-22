from surprise import Reader, Dataset
from surprise import KNNBasic
from surprise.model_selection import cross_validate
import pandas as pd


if __name__ == "__main__":
    ratings = pd.read_csv("리뷰데이터크롤링.csv", encoding="cp949")
    # ratings = pd.read_csv("리뷰데이터크롤링(모두보기).csv", encoding="cp949")
    # print(ratings.loc[0])
    ratings.columns = ['review_id', 'book_id', 'nickname',
                       'score', 'sympathy', 'regtime', 'content']
    # ratings.columns = ['review_id', 'book_id', 'user_id', 'nickname',
    #                    'score', 'sympathy', 'regtime', 'content']
    ratings.drop(index=0, inplace=True)
    print(ratings)

    print(ratings['score'].min())
    print(ratings['score'].max())

    reader = Reader(rating_scale=(1.0, 5.0))
    data = Dataset.load_from_df(
        ratings[['nickname', 'book_id', 'score']], reader)
    # data = Dataset.load_from_df(
    #     ratings[['user_id', 'book_id', 'score']], reader)

    print(data)

    algo = KNNBasic()
    cross_validate(algo, data, measures=['RMSE'], cv=5, verbose=True)
