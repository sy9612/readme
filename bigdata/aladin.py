from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
url = 'https://www.aladin.co.kr/shop/wbrowse.aspx?CID=1&BrowseTarget=HighCustReview'
driver.get(url)
# browse7 = driver.find_element_by_id('browse7')
# browse7.click()
# best_reviews = driver.find_element_by_partial_link_text('최고평점도서')
# best_reviews.click()
a_list = driver.find_elements_by_class_name('bo')
bid_list = []
for href in a_list:
    bid_list.append(href.get_attribute("href").split("=")[1])

idx = 0
for bid in bid_list:
    idx += 1
    if idx == 1:
        continue
    link = "https://www.aladin.co.kr/shop/wproduct.aspx?ItemId=" + bid
    driver.get(link)
    html = driver.page_source #현재 페이지 소스 가져오기
    bs = BeautifulSoup(html, "html.parser")
    book_info = []
    # print(bs.prettify())
    result = bs.find('div', class_='Ere_prod_mconts_box')
    # print(result)
    text = bs.select('.Ere_prod_mconts_box > .Ere_prod_mconts_LL').get_text()
    print(text)
    # items = bs.find(bs['script'])
    # print(items)



