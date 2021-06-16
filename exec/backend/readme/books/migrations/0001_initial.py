# Generated by Django 3.1.7 on 2021-04-05 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_isbn', models.CharField(max_length=45)),
                ('book_title', models.CharField(max_length=60)),
                ('book_author', models.CharField(max_length=45)),
                ('book_publisher', models.CharField(max_length=60)),
                ('book_description', models.TextField(blank=True, null=True)),
                ('book_pubdate', models.CharField(blank=True, max_length=60, null=True)),
                ('book_pages', models.IntegerField(blank=True, null=True)),
                ('book_price', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_book',
                'managed': True,
            },
        ),
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
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BooksMaincategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'books_maincategory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='BooksSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=45, null=True)),
                ('main', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'books_subcategory',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('report_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('book_name', models.CharField(max_length=60)),
                ('report_content', models.TextField(max_length=1000)),
                ('report_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('book_id', models.IntegerField()),
                ('review_rating', models.IntegerField()),
                ('review_content', models.TextField(max_length=200)),
                ('review_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]