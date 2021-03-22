from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import csv
import time
import re

review_list = []


def get_book_id(cid):
    # 1. 3점 이상 평점이 많은 순으로 100개의 책 리스트
    url = f'https://www.aladin.co.kr/shop/wbrowse.aspx?CID={cid}&BrowseTarget=HighCustReview'

    req = requests.get(url)

    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # 100개의 책에 대해 id를 리스트로 저장
    book_id_list = []
    for href in soup.select('a.bo'):
        book_id_list.append(href.attrs['href'].split("=")[1])

    return book_id_list


def get_book_id_from_all(cid):
    # 2. 모두 보기 리뷰 많은 순으로 N개
    book_num = 500
    url = f'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount={book_num}&\
            ViewType=Detail&PublishMonth=0&SortOrder=4&page=1&Stockstatus=1&PublishDay=84&CID={cid}\
            &CustReviewRankStart=&CustReviewRankEnd=&CustReviewCountStart=&CustReviewCountEnd=\
            &PriceFilterMin=&PriceFilterMax=&SearchOption='

    req = requests.get(url)

    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # 100개의 책에 대해 id를 리스트로 저장
    book_id_list = []
    for item in soup.select('div.ss_book_box'):
        book_id_list.append(item.attrs['itemid'])

    print(book_id_list)

    return book_id_list


def get_review(book_id_list):

    # 책 정보 페이지
    for book_id in book_id_list:
        url = get_url(book_id)
        referer = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=' + book_id

        custom_header = {
            'referer': referer,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
        }

        # 많은 트래픽을 일으킬 경우 서버에서 요청을 거절할 수 있음.
        # 거절된 경우 2초의 대기시간 후 다시 요청
        try:
            req = requests.get(url, headers=custom_header)
        except:
            time.sleep(2)
            req = requests.get(url, headers=custom_header)

        if req.status_code == requests.codes.ok:
            print(book_id + " 접속 성공")

        req_content = req.content
        soup = BeautifulSoup(req_content, 'html.parser')

        global review_list
        for hl in soup.select('div.hundred_list'):
            # hl : 리뷰 한 개
            # print(hl)
            hlw = hl.select_one('div.HL_write')
            # 유저 닉네임, 공감, 작성날짜
            # nickname = hlw.find('div', {'class': 'left'}).find(
            #     'a', {'class': 'Ere_PR10'}).text
            user = hlw.select_one('div.left > a.Ere_PR10')
            if user == None:
                continue
            uid = user.attrs['href'].split('/')[3]
            nickname = user.text
            info = hlw.select('div.left > span.Ere_PR10')
            reg_time = info[0].text
            # 공감 (15) 에서 숫자만 뽑아오기
            sympathy = re.findall("\d+", info[1].text)[0]

            # 스포일러가 안들어간 리뷰 내용 and 개행문자 및 공백제거
            # content = hlw.find('div', {'style': 'display:'}).text.strip()
            content = hlw.select_one(
                'div[style=display\:]').text.replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()

            # 평점 1 ~ 5
            score = 0
            for star in hl.select('div.HL_star > img'):
                # 별이 있는 경우
                if star.attrs['src'][-5] == 'n':
                    score += 1

            if book_id and uid and nickname and score and content:
                review_list.append(
                    [book_id, uid, nickname, score, sympathy, reg_time, content])


def get_url(book_id):
    # IsOrderer=1 : 구매자 리뷰
    # IsOrderer=2 : 전체 리뷰
    item_id = book_id
    # page_count : 최대로 불러올 리뷰 개수
    page_count = 1000
    url = f'https://www.aladin.co.kr/ucl/shop/product/ajax/GetCommunityListAjax.aspx?ProductItemId={item_id}&itemId={item_id}\
    &pageCount={page_count}&communitytype=CommentReview&nem o Type=-1&page=1&startNumber=1&endNumber=10&sort=2&IsOrderer=1&BranchType=1&IsAjax=true&pageType=0'
    return url


if __name__ == "__main__":
    # cid : 카테고리 id
    cid_list = ["1", "112011", "55889", "656", "798",
                "74", "987", "517", "1237", "170", "336"]
    # cid_list = ["1"]
    for cid in cid_list:
        # book_id_list = get_book_id(cid)
        book_id_list = get_book_id_from_all(cid)
        get_review(book_id_list)
    # get_review(['4092522'])
    data = pd.DataFrame(review_list)
    data.columns = ['book_id', 'user_id', 'nickname',
                    'score', 'sympathy', 'regtime', 'content']
    # data.to_csv('리뷰데이터크롤링.csv', sep='\t')
    data.to_csv('리뷰데이터크롤링(모두보기).csv', sep='\t')
    # string = "https://blog.aladin.co.kr/767031116".split('/')
    # print(string)
