"""untitled2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main', main, name='main'),
    url(r'^^$', main, name='main'),
    url(r'^Gallery/', subs_view.as_view(), name='test_url'),
    url(r'^Nature/', h3, name='h3'),
    url(r'^about/', about, name='about'),
    url(r'^notif/', notif, name='notif'),
    url(r'^reg/', reg.as_view(), name='reg'),
    url(r'^auth/', auth1.as_view(), name='auth'),
]
