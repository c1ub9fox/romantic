from rest_framework import serializers
from cmdb.models import DEVICE

# class CmdbSerializer(serializers.Serializer):
#
#     sequence_number = serializers.CharField(source="sn",max_length=128,default=None)
#     device_name = serializers.CharField(source="name",max_length=128)
#     ip_address = serializers.IPAddressField(source="ip",default=None)
#     date = serializers.DateField(default=None)
#     status = serializers.BooleanField()
#
#     def create(self, validated_data):
#         try:
#             instance = DEVICE.objects.create(**validated_data)
#             return instance
#         except Exception as e:
#             print(e)
#             return None
#
#     def update(self, instance, validated_data):
#         try:
#             DEVICE.objects.filter(pk=instance.pk).update(**validated_data)
#             instance = DEVICE.objects.get(pk=instance.pk)
#             return instance
#         except Exception as e:
#             print(e)
#             return None

class CmdbSerializer(serializers.ModelSerializer):

    class Meta:
        model = DEVICE
        fields = '__all__'