# 📚 README 📚

**README**는 콘텐츠 기반 필터링, 협업 필터링, **README**만의 BBTI 기반 추천 리스트를 제공해주는 **"개인 맞춤형 도서 추천 서비스"** 입니다.

`내가 세계를 알게 된 것은 책에 의해서였다. - 사르트르`

`그리고, 책을 알게 된 것은 README에 의해서였다.`

README는 콘텐츠 기반 필터링, 협업 필터링, MBTI 기반 추천 리스트를 제공해주는 **"개인 맞춤형 도서 추천 서비스"** 입니다. 

## 실행 방법

- **BackEnd**
```
cd backend/readme
python -m venv venv
venv\Scripts\activate
pip install django
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

- **FrontEnd**
```
cd FE/readme
npm install
npm run serve
```


## 기술 스택

>🔧**FrontEnd** -  Vue.js

>🔧**BackEnd** -  Django

>🔧**Database**-  MySQL

>🔧**Deploy**-  AWS, Docker



## 추천 알고리즘 분석

### 협업 필터링 - 전처리
![협업 필터링 - 전처리](./bigdata/빅데이터_캡쳐/협업 필터링 - 전처리.PNG)

10개 이상의 리뷰를 남긴 유저 및 15개 이상의 리뷰가 달린 책을 남기는 필터링을 진행하였습니다.

### 협업 필터링 - 알고리즘 테스트
![협업 필터링 - 알고리즘 테스트](./bigdata/빅데이터_캡쳐/협업 필터링 - 알고리즘 테스트.PNG)

알고리즘 테스트 결과 훈련시간이 짧고 정확도가 높은 SVD(Singular Value Decomposition)알고리즘을 채택하였습니다.

### 협업 필터링 - 예측평점 예시
![협업 필터링 - 예측평점 예시](./bigdata/빅데이터_캡쳐/협업 필터링 - 예측평점 예시.PNG)

## 협업 필터링 적용 과정
>1. DB에서 리뷰 10개 이상인 유저 데이터 가져오기
>2. 기존 리뷰 데이터에 추가 후, 예측평점을 구함
>3. top 10 추천 결과를 DB에 저장

## 컨텐츠 기반 필터링

### 컨텐츠 기반 필터링 - 도서간 유사성 평가
![컨텐츠 기반 필터링 - 도서간 유사성 평가](./bigdata/빅데이터 캡처/컨텐츠 기반 필터링 - 도서간 유사성 평가.jpg)

tf-idf알고리즘을 이용하여 도설별 키워드를 추출한 후, 코싸인 유사도를 이용하여 도서간 유사성을 평가하였습니다.

### 컨텐츠 기반 필터링 - 유사도 내림차순 후 10개 추출
![컨텐츠 기반 필터링 - 유사도 내림차순 후 10개 추출](./bigdata/빅데이터 캡처/컨텐츠 기반 필터링 - 유사도 내림차순 후 10개 추출.jpg)

유사도가 높은 순서대로 내림차순 정렬 후, 상위 10개를 추출하여 DB에 저장하고 가져오는 방식으로 추천해줍니다. 


