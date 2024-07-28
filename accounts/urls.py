from django.urls import path
from .views import FirstTimeChoiceView, MatchPreferenceCreateView, RegisterView, LoginView, logout_user, UpdateUserProfileView, EmploymentRegistrationView

app_name = "accounts"

urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('update-profile/', UpdateUserProfileView.as_view(), name='update_profile'),
    path("employment-registration/", EmploymentRegistrationView.as_view(), name="employment_registration"),
    path('first-time-choice/', FirstTimeChoiceView.as_view(), name='first_time_choice'),
    path('match-preference/', MatchPreferenceCreateView.as_view(), name='match_preference_create'),
    path('logout/', logout_user, name='logout'), 
]
