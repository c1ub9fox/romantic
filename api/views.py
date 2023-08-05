from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse
from cmdb.models import DEVICE
from django.forms.models import model_to_dict
from rest_framework.views import APIView

# Create your views here.

# class CmdbView(View):
#
#     def get(self,request):
#
#         response = DEVICE.objects.all().values()
#         return HttpResponse(response)
#
#     def post(self,request):
#
#         return HttpResponse("POST请求")

class CmdbView(APIView):

    def get(self,request):

        response = DEVICE.objects.all().values()
        return HttpResponse(response)

    def post(self,request):

        return HttpResponse("POST请求")