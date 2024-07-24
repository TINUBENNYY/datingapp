from django.urls import path
from .views import RegisterView, LoginView, logout_user, UpdateUserProfileView, EmploymentRegistrationView

app_name = "accounts"

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path("update-profile/", UpdateUserProfileView.as_view(), name="update_profile"),
    path("employment-registration/", EmploymentRegistrationView.as_view(), name="employment_registration"),
    path('logout/', logout_user, name='logout'), 
]
