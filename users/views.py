from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import *

class IndustriesApiList(ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer
