from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('get_persons', get_persons),
    path('get_relations', get_relations)
]
