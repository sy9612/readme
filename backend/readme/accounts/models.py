from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class User(AbstractUser):
    objects = UserManager(
    )  # blank=True: 폼(입력양식)에서 빈채로 저장되는 것을 허용, DB에는 ''로 저장 # CharField 및 TextField는 blank=True만 허용, null=True 허용 X
    nickname = models.CharField(blank=True, max_length=50)
    gender = models.CharField(max_length=5)
    mbti_id = models.IntegerField()
    birth = models.DateField()


class Dibs(models.Model):
    dibs_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=45,blank=True, null=True)
    dibs_date = models.DateTimeField(blank=True, null=True)
    is_selected = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts_dibs'
