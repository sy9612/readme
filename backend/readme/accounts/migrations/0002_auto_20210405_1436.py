# Generated by Django 3.1.7 on 2021-04-05 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dibs',
            name='book_id',
        ),
        migrations.AddField(
            model_name='dibs',
            name='book_isbn',
            field=models.CharField(blank=True, max_length=45, null=True),
        ),
    ]
