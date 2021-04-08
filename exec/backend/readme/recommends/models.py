from django.db import models


class CollaborativeRecommendBook(models.Model):
    # Auto Increment
    collaborative_recommend_book_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_collaborative'

# class ContentRecommendBook(models.Model):
#     content_recommend_book_id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField()
#     book_isbn = models.CharField(max_length=45)

#     class Meta:
#         managed = True
#         db_table = 'recommends_content'


class BestSeller(models.Model):
    bestseller_id = models.AutoField(primary_key=True)
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_bestseller'


class ContentsBasedBooks(models.Model):
    contents_id = models.AutoField(primary_key=True)
    main_isbn = models.CharField(max_length=45)
    relative_isbn1 = models.CharField(max_length=45)
    relative_isbn2 = models.CharField(max_length=45)
    relative_isbn3 = models.CharField(max_length=45)
    relative_isbn4 = models.CharField(max_length=45)
    relative_isbn5 = models.CharField(max_length=45)
    relative_isbn6 = models.CharField(max_length=45)
    relative_isbn7 = models.CharField(max_length=45)
    relative_isbn8 = models.CharField(max_length=45)
    relative_isbn9 = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_content'

class AgeGenderRecommendBook(models.Model):
    agegender_recommend_book_id = models.AutoField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=5)
    book_isbn = models.CharField(max_length=45)

    class Meta:
        managed = True
        db_table = 'recommends_age_gender'