# Generated by Django 3.1.7 on 2021-04-07 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbtis', '0002_auto_20210405_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mbtibook',
            name='mbti_id',
        ),
        migrations.AddField(
            model_name='mbtibook',
            name='one_of_mbti_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]