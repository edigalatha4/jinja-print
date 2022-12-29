from django.urls import path
from app2.views import *
app_name='something1'

urlpatterns=[
    path('second/',second,name='second'),
    path('third/',third,name='third'),
]