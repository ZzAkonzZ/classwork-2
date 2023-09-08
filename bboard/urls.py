from django.urls import path

from bboard.views import *

urlpatterns = [
    path('', index),
]
