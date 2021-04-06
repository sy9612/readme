from rest_framework.pagination import PageNumberPagination

# Custom PageNumberPagination
class CarouselPageNumberPagination(PageNumberPagination):
    # 페이지 당 보여줄 아이템의 개수를 25개로 지정
	page_size = 16