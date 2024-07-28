from django.urls import path
from .views import IndexView, user_profiles_view

app_name = "user"

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profiles/', user_profiles_view, name='user_profiles'),
]
