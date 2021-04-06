from django.db import models

class CollaborativeRecommendBook(models.Model):
    # Auto Increment
    collaborative_recommend_book_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_collaborative'

class ContentRecommendBook(models.Model):
    content_recommend_book_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_content'

class BestSeller(models.Model):
    bestseller_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_bestseller'