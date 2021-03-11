from urllib.request import urlopen
import json

isbns = ["9788965880776"]
for isbn in isbns:
    url = "http://data4library.kr/api/keywordList?authKey=d259799ad80022b12c5e3c40ce7b14715ea0b9416d27ec668a2a411715d8c8f8&isbn13="+isbn+"&additionalYN=Y&format=json"
    responseBody = urlopen(url).read().decode('utf-8')
    jsonArray = json.loads(responseBody)
    # # print(jsonArray)
    resultNum = jsonArray.get("response").get("resultNum")
    if resultNum == 0:
        print("no item")
    else:
        items = jsonArray.get("response").get("items")
        additionalItems = jsonArray.get("response").get("additionalItem")
        bookname = additionalItems.get("bookname")
        print(bookname)
        idx = 0
        for list in items:
            idx += 1
            word = list.get("item").get("word")
            weight = list.get("item").get("weight")
            print(str(idx) + " word: " + word +" weight: " + weight)
        print()
    # resultNum = jsonArray.get("resultNum")
    # print(resultNum)
    # for i in resultNum:
    #     word = jsonArray.get("word")
    #     weight = jsonArray.get("weight")
    #     print("word: " + word +" weight: " + weight)


