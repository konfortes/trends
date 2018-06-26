from rest_framework import serializers
from trends.models import Keyword


class KeywordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Keyword
        fields = ('name', 'is_active')