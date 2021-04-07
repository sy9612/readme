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


def get_book_id_from_all(cid, book_num=100):
    # 2. 모두 보기 구매 많은 순으로 N개
    url = f'https://www.aladin.co.kr/shop/wbrowse.aspx?BrowseTarget=List&ViewRowsCount={book_num}&\
            ViewType=Detail&PublishMonth=0&SortOrder=2&page=1&Stockstatus=1&PublishDay=84&CID={cid}'

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

        # book_isbn 가져오기
        try:
            req = requests.get(referer)
        except:
            time.sleep(2)
            req = requests.get(referer)
        soup = BeautifulSoup(req.content, 'html.parser')
        # book_isbn = str(soup.select('div.conts_info_list1 > ul > li')[3].text).split(':')[1].strip()
        book_isbn = soup.find('meta', property = "books:isbn")
        if book_isbn is None:
            continue
        book_isbn = book_isbn["content"]
        
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
            nickname = user.text.strip()
            # info = hlw.select('div.left > span.Ere_PR10')
            # reg_time = info[0].text
            # 공감 (15) 에서 숫자만 뽑아오기
            # sympathy = re.findall("\d+", info[1].text)[0]

            # 스포일러가 안들어간 리뷰 내용 and 개행문자 및 공백제거
            # content = hlw.find('div', {'style': 'display:'}).text.strip()
            # content = hlw.select_one(
            #     'div[style=display\:]').text.replace("\t", " ").replace("\r", " ").replace("\n", " ").strip()

            # 평점 1 ~ 5
            score = 0
            for star in hl.select('div.HL_star > img'):
                # 별이 있는 경우
                if star.attrs['src'][-5] == 'n':
                    score += 1

            if book_id and uid and nickname and score:
                review_list.append(
                    [book_id, book_isbn, uid, nickname, score])


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
    # cid_list = ["1", "112011", "55889", "656", "798",
    #             "74", "987", "517", "1237", "170", "336"]
    fiction_cid_list = [50926, 50928, 50929, 50930, 50931, 50932, 50933, 50935]
    cid_list = [51371, 51373, 174700, 51374, 51375, 51376, 51377, 51380, 51842, 51389, 51391, 51392, 51394, 70214, 70212, 70211, 2951, 70236, 107822, 70224, 70233, 70228, 70220, 70223, 2943, 3057, 2172, 2028, 261, 172, 177, 3049, 51002, 51005, 51007, 51010, 51013, 51015, 51017, 51272, 51275, 51022, 51024, 51027, 51030, 51033, 51035, 51038, 51039, 51043, 51045, 65237, 51378, 51381, 51384, 51387, 51390, 51393, 51395, 51399, 51403, 51412, 51415, 51417, 50992,
                50995, 50997, 50999, 51001, 51004, 51008, 51011, 51026, 51037, 51041, 51046, 50874, 50875, 50876, 50877, 50878, 50880, 50881, 50882, 50883, 50884, 50885, 50886, 50887, 50888, 50889, 50890, 88, 27795, 2032, 5618, 89, 90, 2211, 5566, 4167, 17897, 84, 52620, 1963, 5718, 134, 87, 9671, 50758, 1150, 2012, 2574, 7268, 1143, 4410, 1141, 32399, 1139, 1142, 32663, 28969, 1149, 51564, 51565, 51566, 51567, 51568, 51569, 51570, 50950, 50965, 50966, 50967, 50968, 50969, 50970, 50971, 50972, 50973, 50974, 50975, 50976]

    for cid in fiction_cid_list:
        # 장르소설은 250개씩 가져옴
        book_id_list = get_book_id_from_all(str(cid), 250)
        get_review(book_id_list)

    for cid in cid_list:
        # book_id_list = get_book_id(cid)
        book_id_list = get_book_id_from_all(str(cid), 250)
        get_review(book_id_list)
    # get_review(['264270055'])
    data = pd.DataFrame(review_list)
    data.columns = ['book_id', 'book_isbn', 'user_id', 'nickname',
                    'score']
    print(data)
    # data.to_csv('리뷰데이터크롤링.csv', sep='\t')
    # data.to_csv('리뷰데이터크롤링(모두보기).csv', sep='\t', encoding='utf-8-sig')
    data.to_pickle('./data/리뷰데이터크롤링(모두보기).pkl')
    # data.to_pickle('./data/리뷰데이터크롤링(모두보기)_sample.pkl')
