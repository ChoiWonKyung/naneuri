"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf.urls import url
from .contactlist import views

from .api.views import index_view, MessageViewSet

router = routers.DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [

    # http://localhost:8000/
    path('',  views.address_list, name='index'),

    # http://localhost:8000/api/<router-viewsets>
    path('api/', include(router.urls)),

    # http://localhost:8000/admin/
    path('admin/', admin.site.urls),

    path('addresses/', views.address_list),
    path('addresses/<int:pk>/', views.address),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
