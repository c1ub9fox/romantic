
from django.urls import path,re_path
from .views import CmdbView,CmdbDetailView

urlpatterns = [
    path('cmdb/', CmdbView.as_view()),
    # re_path('cmdb/(\d+)',CmdbDetailView.as_view())
    re_path('cmdb/(?P<pk>\d+)',CmdbDetailView.as_view())
]