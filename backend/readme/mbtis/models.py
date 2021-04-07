from django.db import models


class MBTIBook(models.Model):
    mbti_book_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45)
    mbti_id = models.IntegerField()


class MBTI(models.Model):
    mbti_id = models.AutoField(primary_key=True)
    mbti_type = models.CharField(max_length=10)
    mbti_desc = models.TextField(blank=True, max_length=400)