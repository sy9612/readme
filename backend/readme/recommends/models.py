from django.db import models

class CollaborativeRecommendBook(models.Model):
    # Auto Increment
    collaborative_recommend_book_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)

class ContentRecommendBook(models.Model):
    content_recommend_book_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)

class BestSeller(models.Model):
    best_seller_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45)
    book_title = models.CharField(max_length=60)
    book_author = models.CharField(max_length=45)
    book_publisher = models.CharField(max_length=60)
    book_pubdate = models.CharField(max_length=60, blank=True, null=True)
    book_pages = models.IntegerField(blank=True, null=True)
    book_price = models.IntegerField(blank=True, null=True)