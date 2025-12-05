from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .serializers import *
from drf_spectacular.utils import extend_schema
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView


from .serializers import RoomSerializer
 
class RoomCreate(APIView):
    pass
 
class RoomUpdateDelete(APIView):
    pass