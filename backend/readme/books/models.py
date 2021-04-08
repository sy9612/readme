from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45)
    book_title = models.CharField(max_length=100)
    book_author = models.CharField(max_length=100)
    book_publisher = models.CharField(max_length=100)
    book_description = models.TextField(blank=True, null=True)
    book_pubdate = models.CharField(max_length=100, blank=True, null=True)
    book_pages = models.IntegerField(blank=True, null=True)
    book_price = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books_book'
        # SELECT WHERE 절에 많이 사용되는 book_isbn 컬럼을 인덱스로 지정해
        # SELECT 쿼리의 성능을 높임
        indexes = [
            models.Index(fields=['book_isbn',]),
        ]


class BooksCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45, blank=True, null=True)
    main_category = models.IntegerField(blank=True, null=True)
    sub_category = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books_category'


class BooksMaincategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books_maincategory'


class BooksSubcategory(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    main = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'books_subcategory'


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)
    book_name = models.CharField(max_length=100)
    report_content = models.TextField(max_length=1000)
    report_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45,blank=True, null=True)
    review_rating = models.IntegerField()
    review_content = models.TextField(max_length=200)
    review_date = models.DateTimeField(auto_now_add=True)