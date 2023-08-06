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

    def create(self, validated_data):
        try:
            instance = DEVICE.objects.create(**validated_data)
            return instance
        except Exception as e:
            print(e)
            return None

    def update(self, instance, validated_data):
        try:
            DEVICE.objects.filter(pk=instance.pk).update(**validated_data)
            instance = DEVICE.objects.get(pk=instance.pk)
            return instance
        except Exception as e:
            print(e)
            return None


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
        cmdb_serializer.save()
        return Response(cmdb_serializer.data)


class CmdbDetailView(APIView):

    def get(self,request,id):

        cmdb_query = DEVICE.objects.get(pk=id)
        cmdb_serializer = CmdbSerializer(instance=cmdb_query,many=False)
        return Response(cmdb_serializer.data)
    def put(self,request,id):

        put_data = request.data
        cmdb_query = DEVICE.objects.get(pk=id)
        cmdb_serializer = CmdbSerializer(instance=cmdb_query,data=put_data)
        if not cmdb_serializer.is_valid():
            return Response(cmdb_serializer.errors)
        cmdb_serializer.save()
        return Response(cmdb_serializer.data)
    def delete(self,request,id):
        pass



