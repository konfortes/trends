# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from trends.models import Keyword
from trends.serializers import KeywordSerializer

@api_view(['GET'])
def stam(request):
    return Response('Hey!')


@api_view(['GET'])
def keywords_collection(request):
    if request.method == 'GET':
        keywords = Keyword.objects.all()
        serializer = KeywordSerializer(keywords, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def keyword_element(request, pk):
    try:
        keyword = Keyword.objects.get(pk=pk)
    except Keyword.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = KeywordSerializer(keyword)
        return Response(serializer.data)