from django.urls import path
from . import views

urlpatterns = [
  path('', views.NoticeAPIView.as_view()),
]