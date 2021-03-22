from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=60)
    book_author = models.CharField(max_length=45)
    book_publisher = models.CharField(max_length=60)
    book_desc = models.TextField(blank=True, null=True)
    category_id = models.IntegerField()
    book_category = models.CharField(max_length=45)
    book_images = models.IntegerField(blank=True, null=True)
    book_pages = models.IntegerField(blank=True, null=True)


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=60)


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=60)
    report_content = models.TextField(max_length=1000)
    report_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    review_rating = models.IntegerField()
    review_content = models.TextField(max_length=200)
    review_date = models.DateTimeField(auto_now_add=True)