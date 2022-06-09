"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from coviddig.views import main_page
from coviddig.views import circle
from coviddig.views import 마스크착용시도별
from coviddig.views import vaccine1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_page),
    path('circle/', circle),
    path('cbc/', 마스크착용시도별),
    path('vc1/', vaccine1)
]
