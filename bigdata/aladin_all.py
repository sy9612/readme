import time
import requests
from bs4 import BeautifulSoup
import pymysql
import urllib.request
import pandas as pd
import csv
from tempfile import TemporaryFile

def get_book_id(cid_list):
    # 임시 저장소에 뭐 있는지 확인
    temp_storage.seek(0)
    data = temp_storage.read()

    if data is '':
        s_page = 1
        s_cid = 0
    else:
        pg_cd = data.split(",")
        if int(pg_cd[0]) == 10:
            s_page = 1
            s_cid = int(pg_cd[1]) + 1
        else:
            s_page = int(pg_cd[0]) + 1
            s_cid = int(pg_cd[1])

            #카테고리 분류 cid
    for i in range(s_cid, len(cid_list)):
        print(i)
        cid = cid_list[i]
        print("########## CID : " + str(cid) + " #########")
        for page in range(s_page,11):#1페이지부터 5페이지까지
            url = "https://www.aladin.co.kr/shop/wbrowse.aspx?&ViewRowsCount=25&CID=" + str(cid) + "&page=" + str(page)
            print("########## " + str(page) + "페이지 #########")
            req = requests.get(url)
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')

            bid_list = []
            for href in soup.select('a.bo3'):
                bid_list.append(href.attrs['href'].split("=")[1])
            get_book_info(bid_list=bid_list, cid=cid)
            conn.commit()
            for list in csv_lists:
                wr.writerow(list)
            csv_lists.clear()

            # 크롤링하던 페이지와 카테고리 임시 저장
            temp_storage.seek(0)
            temp_storage.write(str(page))
            temp_storage.write(",")
            temp_storage.write(str(i))
            data = temp_storage.read()
            print(data)


def get_book_info(bid_list, cid):
    idx = 0
    for bid in bid_list:
        idx += 1
        # bid = str(399757)
        link = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + bid
        print(link)

        req = requests.get(link)
        req_content = req.content

        # print(req_content)
        soup = BeautifulSoup(req_content, 'html.parser')
        #이미지 저장
        try:
         img_url = soup.find("meta", property="og:image")['content']
        except:
            continue
        urllib.request.urlretrieve(img_url, "./img/" + bid + '.jpg')

        #출판사, 페이지, 등등 찾아오기
        tmps = soup.find("script", type = "application/ld+json")
        if tmps is None:
            continue
        for tmp in tmps:
            # print(tmp)
            #출판사
            tmp1 = tmp.split("publisher")
            tmp2 = tmp1[1].split("name\":\"")
            book_publisher = tmp2[1].split("\"")[0]
            # print(tmp2[1])
            #isbn
            tmp3 = tmp2[1].split("isbn\": \"")
            book_isbn = tmp3[1].split("\"")[0]
            # 출판날짜
            tmp4 = tmp3[1].split("datePublished\": \"")
            book_pubdate = tmp4[1].split("\"")[0]
            # print(book_pubdate)
            #가격
            tmp5 = tmp4[1].split("Price\":")
            book_price = tmp5[1].split(",")[0]
            book_price = int(book_price)
            # print(book_price)

        book_title = soup.find("meta", property="og:title").attrs["content"]
        book_author = soup.find("meta", property="og:author").attrs["content"]

        basic_info = soup.find('div', class_='conts_info_list1')
        texts = basic_info.select('li')
        for text in texts:
            page = text.get_text()
            tmp = page.find('쪽')
            # print(page)
            if tmp is not -1:
                break
        try:
         book_pages = int(page.split("쪽")[0])
        except:
            book_pages = 0

        link = 'https://www.aladin.co.kr/shop/product/getContents.aspx?ISBN=' + book_isbn + '&name=Introduce&type=0&date=22'
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
        if req_content is None:
            continue
        soup = BeautifulSoup(req_content, 'html.parser')
        books_info = soup.select(".Ere_prod_mconts_box > .Ere_prod_mconts_LS")
        books = soup.select(".Ere_prod_mconts_box > .Ere_prod_mconts_R")
        idx2 = 0
        for book_info in books_info:
            if book_info.get_text() == '책소개':
                # print(book_info.get_text())
                # print(books[idx].get_text())
                book_description = books[idx2].get_text()
                book_description = book_description.replace("\r\n", "")
            idx2 += 1
        else:
            book_description = ""

        # print(idx)
        # print("페이지: " + str(book_pages) + "쪽 /isbn: " + book_isbn)
        # print("책이름: " + book_title + " /작가 : " + book_author + " /출판사 : " + book_publisher)
        # print("책내용: " + book_description)
        book_maincategory = mid
        book_subcategory = cid
        # print(book_maincategory)
        # print(book_subcategory)
        # print(type(book_maincategory))
        # print(type(book_subcategory))

        sql = """INSERT INTO books_book
        (book_isbn, book_title, book_author, book_publisher, book_description, book_pubdate, book_pages, book_price)
            values (%s, %s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(sql,
                       (book_isbn, book_title, book_author, book_publisher, book_description, book_pubdate, book_pages, book_price))
        sql = """INSERT INTO books_category(book_id, main_category, sub_category)
        values (%s, %s, %s)"""
        cursor.execute(sql, (book_isbn, book_maincategory, book_subcategory))

        ##################csv 파일 만들기##################
        csv_list = []
        csv_list.append(book_isbn)
        csv_list.append(book_title)
        csv_list.append(book_description)
        print(csv_list)
        csv_lists.append(csv_list)

csv_lists = []
if __name__ == "__main__":
    temp_storage = open("temp.txt", "r+")
    f = open("book_data.csv", "a", encoding='euc-kr', newline='')

    wr = csv.writer(f)
    # wr.writerow(["book_isbn", "book_title", "book_description"])
    conn = pymysql.connect(host='j4a205.p.ssafy.io', user='ssafy', db='readme', password='ssafy', charset='utf8')
    cursor = conn.cursor()
    mid = 1
    cid_list = [50926, 50928, 50929, 50930, 50931, 50932, 50933, 50935]
    # print(cid_list)
    get_book_id(cid_list=cid_list)
    #
    # data = pd.DataFrame(csv_lists)
    # data.columns = ["book_isbn", "book_title", "book_description"]
    # data.to_csv('book_data.csv', index=False, encoding='euc-kr')
