from rest_framework.serializers import *

from .models import *


class IndustrySerializer(ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'


class LocateSerializer(ModelSerializer):
    region = ReadOnlyField(source='region_id.title')
    class Meta:
        model = Locate
        fields = ['id' ,'region', 'title', 'population']