from rest_framework.serializers import *

from .models import *


class IndustrySerializer(ModelSerializer):
    class Meta:
        model = Industry
        fields = '__all__'
