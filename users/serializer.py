import io

from rest_framework import  serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import *

class LocateModel:
    def __init__(self  , region , title, population):

        self.region = region
        self.title = title
        self.population = population


class LocateSerializerNoModel(serializers.Serializer):
    region = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    population = serializers.IntegerField()


def encode():
    model = LocateModel(18,'Хамамат-Юрт', 44)
    model_sr = LocateSerializerNoModel(model)
    print(model_sr.data, type(model_sr.data), sep='\n')

    json = JSONRenderer().render(model_sr.data)
    print(json)

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class LocateSerializer(serializers.ModelSerializer):
    region = serializers.ReadOnlyField(source='region_id.title')
    class Meta:
        model = Locate
        fields = ['id','region', 'title', 'population']