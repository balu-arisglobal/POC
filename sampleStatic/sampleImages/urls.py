from django.urls import path
from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.model_form_upload),
    path('home', views.model_form_upload),
    path('uploadFiles', views.model_form_upload, name='model_form_upload'),
    path('allFiles', views.get_all_files, name='get_all_files'),
    path('clearAllFiles', views.clear_all_images, name='clear_all_images'),
]


