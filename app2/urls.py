from django.urls import path
from app2.views import venki2
app_name='love'

urlpatterns=[
    path('venki2/',venki2,name='venki2')
]
