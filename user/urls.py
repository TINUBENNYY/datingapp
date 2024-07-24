from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
