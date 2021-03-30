from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import ReportSerializer
from rest_framework.response import Response
from django.db.models import Q
# 상위 폴더 import
import os
import sys
sys.path.append( os.path.dirname(os.path.abspath(os.path.dirname(__file__))) )
from books.models import Report

@api_view(('GET', 'POST'))
def report(request, user_id):
    if request.method == 'GET':
        # .get()은 single object = not iterable
        # .filter() 는 QuerySet = iterable
        report_list = Report.objects.filter(user_id = user_id)
        # many = True : queryset이 여러 개의 아이템을 포함하고 있다.(리스트) 를 장고(DRF)에 알려줌
        serializer = ReportSerializer(report_list, many = True)

    elif request.method == 'POST':
        serializer = ReportSerializer(data = request.data)
        # DRF(Django Rest Framework) 에서는 request에서 데이터를 받을 때
        # 반드시 is_valid() 여부를 체크해야 한다.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    return Response(serializer.data, status = status.HTTP_200_OK)

@api_view(('GET', 'PUT', 'DELETE'))
def report_detail(request, user_id, book_id):
    try:
        report = Report.objects.get(Q(user_id = user_id) & Q(book_id = book_id))
    except Report.DoesNotExist:
        return Response({
            'code' : 404,
            'message' : "Report not found!"
        }, status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReportSerializer(report)
        return Response(serializer.data, status = status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = ReportSerializer(report, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        report.delete()
        # 삭제한 뒤에는 204 NO CONTENT를 리턴
        return Response(status = status.HTTP_204_NO_CONTENT)
