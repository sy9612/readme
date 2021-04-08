from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup

def get_book_id():
    # 1. 3점 이상 평점이 많은 순으로 100개의 책 리스트
    url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=1&BrowseTarget=HighCustReview'

    req = requests.get(url)

    content = req.content

    soup = BeautifulSoup(content, 'html.parser')

    # 100개의 책에 대해 id를 리스트로 저장
    bid_list = []
    for href in soup.select('a.bo'):
        bid_list.append(href.attrs['href'].split("=")[1])
    return bid_list

def get_book_info(bid_list):
    idx = 0
    for bid in bid_list:
        idx += 1
        if idx == 1:
            continue
        link = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + bid
        req = requests.get(link)
        req_content = req.content
        soup = BeautifulSoup(req_content, 'html.parser')
        basic_info = soup.find('div', class_='conts_info_list1')
        text = basic_info.text
        text.split("쪽")
        print(basic_info)
        isbn = "8925556782"
        link = 'https://www.aladin.co.kr/shop/product/getContents.aspx?ISBN=' + isbn + '&name=Introduce&type=0&date=22'
        referer = 'https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=' + bid

        custom_header = {
            'referer': referer,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
        }

        # 많은 트래픽을 일으킬 경우 서버에서 요청을 거절할 수 있음.
        # 거절된 경우 2초의 대기시간 후 다시 요청
        try:
            req = requests.get(link, headers=custom_header)
        except:
            time.sleep(2)
            req = requests.get(link, headers=custom_header)

        if req.status_code == requests.codes.ok:
            print(" 접속 성공")

        req_content = req.content
        soup = BeautifulSoup(req_content, 'html.parser')
        books_info = soup.select(".Ere_prod_mconts_box > .Ere_prod_mconts_LS")
        books = soup.select(".Ere_prod_mconts_box > .Ere_prod_mconts_R")
        idx = 0
        for book_info in books_info:
            if book_info.get_text() == '책소개':
                print(book_info.get_text())
                print(books[idx].get_text())
            idx += 1

if __name__ == "__main__":
    bids = get_book_id()
    get_book_info(bid_list=bids)
