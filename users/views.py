from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializer import *
from rest_framework.generics import *

class IndustriesApiList(APIView):
    def get(self, request, count ,string):
        industies = Industry.objects.filter(title__contains=string)[:count].values()
        return Response({'data': list(industies)})

    def post(self, request):

        industies_new = Industry.objects.create(
            title=request.data['title']
        )
        return Response({'data':model_to_dict(industies_new)})

class LocateApiList(APIView):

    def get(self, request, count ,string):
        locate = Locate.objects.filter(title__contains=string).order_by('-title').order_by("-population")[:count].values()
        return Response({'data': list(locate)})

