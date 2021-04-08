from rest_framework import serializers
from books.models import Report

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['user_id', 'book_isbn', 'report_content']