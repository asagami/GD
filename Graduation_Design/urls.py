"""Graduation_Design URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from webapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^log/(.*)$',views.log),
    url(r'^logout$',views.logout),
    url(r'^signup/$',views.sign_up),
    url(r'^sign/$',views.sign),
    url(r'^chpwd/$',views.chpwd),
    url(r'^chpwd_r$',views.chpwd_r),
    url(r'^about/$',views.about),
    url(r'^manageorder1/$',views.manageorder),
    url(r'^manageuser/$',views.manageuser),
    url(r'^order_yes/$',views.manageorder_yes),
    url(r'^order_no/$', views.manageorder_no),
    url(r'^order_delete/$',views.manageorder_delete),
    url(r'^order_change/$',views.order_change),
    url(r'^managegood/$',views.managegood),
    url(r'^sale/$',views.sale),
    url(r'^buyview/(.*)/$',views.buyview),
    url(r'^shopping/(.*)$',views.shopping),
    url(r'^buy/(.*)$',views.buy),
]

