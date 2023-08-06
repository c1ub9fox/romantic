from django.shortcuts import render
from django.http.response import HttpResponse
from cmdb.models import DEVICE
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import CmdbSerializer
from rest_framework.generics import (
    GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.mixins import (
    ListModelMixin,
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
    UpdateModelMixin,
)


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






# class CmdbView(APIView):
#
#     def get(self,request):
#
#         cmdb_model = DEVICE.objects.all()
#         cmdb_serializer = CmdbSerializer(instance=cmdb_model,many=True)
#         return Response(cmdb_serializer.data)
#
#     def post(self,request):
#
#         post_data = request.data
#         cmdb_serializer = CmdbSerializer(data=post_data)
#         if not cmdb_serializer.is_valid():
#             return Response(cmdb_serializer.errors)
#         cmdb_serializer.save()
#         return Response(cmdb_serializer.data)
#
#
# class CmdbDetailView(APIView):
#
#     def get(self,request,id):
#
#         cmdb_query = DEVICE.objects.get(pk=id)
#         cmdb_serializer = CmdbSerializer(instance=cmdb_query,many=False)
#         return Response(cmdb_serializer.data)
#     def put(self,request,id):
#
#         put_data = request.data
#         cmdb_query = DEVICE.objects.get(pk=id)
#         cmdb_serializer = CmdbSerializer(instance=cmdb_query,data=put_data)
#         if not cmdb_serializer.is_valid():
#             return Response(cmdb_serializer.errors)
#         cmdb_serializer.save()
#         return Response(cmdb_serializer.data)
#     def delete(self,request,id):
#         pass


# class CmdbView(GenericAPIView):
#
#     queryset = DEVICE.objects.all()
#     serializer_class = CmdbSerializer
#
#     def get(self,request):
#
#         serializer = self.get_serializer(instance=self.get_queryset(),many=True)
#         return Response(serializer.data)
#
#     def post(self,request):
#
#         post_data = request.data
#         serializer = self.get_serializer(data=post_data)
#
#         if not serializer.is_valid():
#             return Response(serializer.errors)
#         serializer.save()
#         return Response(serializer.data)
#
#
# class CmdbDetailView(GenericAPIView):
#
#     queryset = DEVICE.objects.all()
#     serializer_class = CmdbSerializer
#
#
#     def get(self,request,pk):
#
#         serializer = self.get_serializer(instance=self.get_object(),many=False)
#         return Response(serializer.data)
#     def put(self,request,pk):
#
#         put_data = request.data
#         serializer = self.get_serializer(instance=self.get_object(),data=put_data)
#         if not serializer.is_valid():
#             return Response(serializer.errors)
#         serializer.save()
#         return Response(serializer.data)
#     def delete(self,request,pk):
#
#         self.get_object().delete()
#         return Response()

# class CmdbView(GenericAPIView,ListModelMixin,CreateModelMixin):
#
#     queryset = DEVICE.objects.all()
#     serializer_class = CmdbSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class CmdbDetailView(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
#
#     queryset = DEVICE.objects.all()
#     serializer_class = CmdbSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request)
#
#     def put(self,request,pk):
#         return self.update(request)
#
#     def delete(self,request,pk):
#         return self.destroy(request)

class CmdbView(ListCreateAPIView):

    queryset = DEVICE.objects.all()
    serializer_class = CmdbSerializer

class CmdbDetailView(RetrieveUpdateDestroyAPIView):

    queryset = DEVICE.objects.all()
    serializer_class = CmdbSerializer
