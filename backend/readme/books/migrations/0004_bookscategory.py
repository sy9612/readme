# Generated by Django 3.1.7 on 2021-03-30 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210326_1148'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooksCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_id', models.CharField(blank=True, max_length=60, null=True)),
                ('main_category', models.IntegerField(blank=True, null=True)),
                ('sub_category', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_category',
                'managed': False,
            },
        ),
    ]