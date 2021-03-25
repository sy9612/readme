import time
import requests
from bs4 import BeautifulSoup
import pymysql
import urllib.request

def get_book_id(cid_list):
    #카테고리 분류 cid
    for cid in cid_list:
        print("########## CID : " + str(cid) + " #########")
        for page in range(1, 50):#1페이지부터 50페이지까지
            url = "https://www.aladin.co.kr/shop/wbrowse.aspx?&ViewRowsCount=50&CID=" + str(cid) + "&page=" + str(page)
            print("########## " + str(page) + "페이지 #########")
            req = requests.get(url)
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')

            bid_list = []
            for href in soup.select('a.bo3'):
                bid_list.append(href.attrs['href'].split("=")[1])
            get_book_info(bid_list=bid_list)

def get_book_info(bid_list):
    idx = 0
    for bid in bid_list:
        idx += 1
        link = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + bid
        print(link)

        req = requests.get(link)
        req_content = req.content
        # print(req_content)
        soup = BeautifulSoup(req_content, 'html.parser')

        #이미지 저장
        img_url = soup.find("meta", property="og:image")['content']
        # print(img_url)
        urllib.request.urlretrieve(img_url, "./img/" + bid + '.jpg')

        #출판사, 페이지, 등등 찾아오기
        tmps = soup.find("script", type = "application/ld+json")
        if tmps is None:
            continue
        for tmp in tmps:
            # print(tmp)
            tmp1 = tmp.split("publisher")
            tmp2 = tmp1[1].split("name\":\"")
            book_publisher = tmp2[1].split("\"")[0]
            # print(tmp2[1])
            tmp3 = tmp2[1].split("isbn\": \"")
            book_isbn = tmp3[1].split("\"")[0]
            # isbn = tmp2[1].split("\"")[0]
            # print("---------------------------------")
            # if tmp == "publisher:":
            #     if "name:" in tmp:
            #         print(tmp)

        # tmp = soup.find("li", class_="Ere_sub2_title").find_all('a', class_="Ere_sub2_title")
        # publisher = tmp[2].text

        book_name = soup.find("meta", property="og:title").attrs["content"]
        book_author = soup.find("meta", property="og:author").attrs["content"]

        basic_info = soup.find('div', class_='conts_info_list1')
        texts = basic_info.select('li')
        for text in texts:
            page = text.get_text()
            tmp = page.find('쪽')
            if tmp is not -1:
                break

        book_pages = int(page.split("쪽")[0])
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
                book_desc = books[idx2].get_text()
            idx2 += 1

        # print(idx)
        # print("페이지: " + str(book_pages) + " isbn: " + book_isbn)
        # print("책이름: " + book_name + " 작가 : " + book_author + " 출판사 : " + book_publisher)
        # print("책내용: " + book_desc)


        # sql = """INSERT INTO books_book(book_name, book_author, book_publisher, book_desc, category_id, book_category, book_pages, book_isbn)
        # values (%s, %s, %s, %s, %s, %s, %s, %s)"""
        # book_id = idx
        # category_id = idx
        # cursor.execute(sql, (book_name, book_author, book_publisher, book_desc, category_id, "?", book_pages, book_isbn))
        # conn.commit()

if __name__ == "__main__":
    conn = pymysql.connect(host='localhost', user='ssafy', db = 'readme', password='ssafy', charset='utf8')
    cursor = conn.cursor()

    cid_list = []
    idx = 50926
    for i in range(10):
        if idx == 50934:
            continue
        cid_list.append(idx)
        idx += 1
    print(cid_list)
    get_book_id(cid_list=cid_list)

