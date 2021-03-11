from bs4 import BeautifulSoup
import requests
import json


def get_book_id():
    # 3점 이상 평점이 많은 순으로 100개의 책 리스트
    url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=1&BrowseTarget=HighCustReview'
    req = requests.get(url)
    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # 100개의 책에 대해 id를 리스트로 저장
    book_id_list = []
    for href in soup.select('a.bo'):
        # print(href.attrs['href'].split("=")[1])
        book_id_list.append(href.attrs['href'].split("=")[1])

    # book_id_list = soup.select('a.bo')

    print(book_id_list)

    return book_id_list


def get_review(book_id_list):
    # IsOrderer=1 : 구매자 리뷰
    # IsOrderer=2 : 전체 리뷰
    url = 'https://www.aladin.co.kr/ucl/shop/product/ajax/GetCommunityListAjax.aspx?ProductItemId=56869333&itemId=56869333\
    &pageCount=10&communitytype=CommentReview&nemoType=-1&page=1&startNumber=1&endNumber=10&sort=2&IsOrderer=1&BranchType=1&IsAjax=true&pageType=0'

    # 책 정보 페이지
    for book_id in book_id_list:
        new_url = url + book_id

        custom_header = {
            'referer': new_url,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }

        req = requests.get(url, headers=custom_header)

        if req.status_code == requests.codes.ok:
            print("접속 성공")
            # print(req.text)
            # review_data = json.loads(req.text)
            # print(review_data)

        content = req.content
        soup = BeautifulSoup(content, 'html.parser')

        for hl in soup.select('div.hundred_list'):
            # print(hl)
            # 평점 1 ~ 5
            score = 0
            for star in hl.select('div.HL_star > img'):
                # 별이 있는 경우
                if star.attrs['src'][-5] == 'n':
                    score += 1
            print(score)


if __name__ == "__main__":
    # book_id_list = get_book_id()
    get_review(['56869333'])
