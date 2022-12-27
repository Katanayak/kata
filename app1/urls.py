from django.urls import path
from app1.views import *

app_name='loveu'

urlpatterns=[
    path('venki/',venki,name='venki')
]