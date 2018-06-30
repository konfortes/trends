# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import  status
from trends.models import Keyword, Trend
from trends.serializers import KeywordSerializer, TrendSerializer

# curl 'localhost:8000/trends/api/v1/keywords'
# curl -X POST -H "Content-Type: application/json" -d '{"name": "Russia"}' 'localhost:8000/trends/api/v1/keywords/'
@api_view(['GET', 'POST'])
def keywords_collection(request):
    if request.method == 'GET':
        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = request.data
        serializer = KeywordSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# curl 'localhost:8000/trends/api/v1/keywords/1'
@api_view(['GET'])
def keyword_element(request, pk):
    try:
        keyword = Keyword.objects.get(pk=pk)
    except Keyword.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = KeywordSerializer(keyword)
        return Response(serializer.data)

# curl 'localhost:8000/trends/api/v1/trends'
@api_view(['GET'])
def trends(request):
    # TODO: caching
    now = datetime.datetime.now()
    # TODO: setting
    outdated_threshold_setting = 7
    outdated_threshold = now - datetime.timedelta(days=outdated_threshold_setting)
    
    # queryset = Trend.objects.filter('last_spotted_at > %s', (outdated_threshold,)).order_by('-score')
    queryset = Trend.objects.filter(last_spotted_at__range=[outdated_threshold, now]).order_by('-score')
    serializer = TrendSerializer(queryset, many=True)
    return Response(serializer.data)
