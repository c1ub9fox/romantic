from django.shortcuts import render
from django.http.response import HttpResponse
from cmdb.models import DEVICE
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response

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

class CmdbSerializer(serializers.Serializer):

    sequence_number = serializers.CharField(source="sn",max_length=128,default=None)
    device_name = serializers.CharField(source="name",max_length=128)
    ip_address = serializers.IPAddressField(source="ip",default=None)
    date = serializers.DateField(default=None)
    status = serializers.BooleanField()

class CmdbView(APIView):

    def get(self,request):

        cmdb_model = DEVICE.objects.all()
        cmdb_serializer = CmdbSerializer(instance=cmdb_model,many=True)
        return Response(cmdb_serializer.data)


    def post(self,request):

        post_data = request.data
        cmdb_serializer = CmdbSerializer(data=post_data)
        if not cmdb_serializer.is_valid():
            return Response(cmdb_serializer.errors)
        try:
            print(cmdb_serializer.data)
            print(cmdb_serializer.validated_data)
            DEVICE.objects.create(**cmdb_serializer.validated_data)
        except Exception as e:
            print(e)
            return Response(data="与现有设备信息冲突，增加设备信息失败")
        return Response(cmdb_serializer.data)
