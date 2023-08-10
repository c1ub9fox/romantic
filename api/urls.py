
from django.urls import path,re_path
from .views import CmdbView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('cmdb',CmdbView)

urlpatterns = [
    # path('cmdb/', CmdbView.as_view({'get': 'list', 'post': 'create'})),
    # re_path('cmdb/(\d+)',CmdbDetailView.as_view())
    # re_path('cmdb/(?P<pk>\d+)',CmdbView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}))
]
urlpatterns += router.urls
