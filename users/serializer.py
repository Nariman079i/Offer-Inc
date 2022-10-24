import io

from rest_framework import  serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class LocateSerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region.title')
    class Meta:
        model = Locate
        fields = ['id','region', 'title', 'population']