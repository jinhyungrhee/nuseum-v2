"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path('api/v1/account/', include('accounts.urls')),
    path('api/v1/consumption/', include('consumptions.urls')),
    path('api/v1/food/', include('foods.urls')),
    path('api/v1/qna/', include("qnas.urls")),
    path('api/v1/notice/', include('notices.urls')),
    path('api/v1/recommendation/', include('recommendations.urls')),
    path('api/v1/result/', include('results.urls')),
]
