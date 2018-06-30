from rest_framework import serializers
from trends.models import Keyword, Trend


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('name', 'is_active')

class TrendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trend
        fields = ('name', 'score')