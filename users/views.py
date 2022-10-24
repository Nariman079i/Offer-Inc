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

class LocateApiList(ListAPIView):

    def get_queryset(self):

        string_ = self.kwargs['string']

        return Locate.objects.filter(title__contains=string_).order_by('-title').order_by("-population")[:10]

    serializer_class = LocateSerializer



