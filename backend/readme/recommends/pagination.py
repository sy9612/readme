from rest_framework.pagination import PageNumberPagination

# Custom PageNumberPagination
class CarouselPageNumberPagination(PageNumberPagination):
    # 캐러셀에 보여줄 아이템의 개수를 10개로 지정
	page_size = 10

class BestSellerPageNumberPagination(PageNumberPagination):
    # 베스트셀러 아이템의 개수를 20개로 지정
	page_size = 20