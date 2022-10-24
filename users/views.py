from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *
from rest_framework.generics import *

class IndustriesApiList(ListAPIView):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class LocateApiList(APIView):

    def get(self, request, count ,string):
        locate = Locate.objects.filter(title__contains=string).order_by('-title').order_by("-population")[:count].values()

        return Response({'data': list(locate)})

