# Generated by Django 3.1.7 on 2021-04-07 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210406_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='book_isbn',
            field=models.CharField(max_length=45),
        ),
    ]
