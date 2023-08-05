
from django.urls import path
from .views import CmdbView

urlpatterns = [
    path('cmdb/', CmdbView.as_view()),
]