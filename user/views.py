from django.shortcuts import render
from django.views.generic import View, TemplateView
from accounts.models import EmploymentProfile, UserProfile
# Create your views here.


class IndexView(TemplateView):
    template_name = "user/index.html"

def user_profiles_view(request):
    profiles = UserProfile.objects.select_related('user').all()
    employment_profiles = EmploymentProfile.objects.select_related('user').all()
    profile_data = []

    for profile in profiles:
        employment = employment_profiles.filter(user=profile.user).first()
        profile_data.append({
            'user' : profile.user,
            'age' : profile.age,
            'location' : employment.location if employment else None,
            'qualification' : profile.qualification,
            'profile_pic' : profile.profile_pic.url if profile.profile_pic else None,
            'description' : f"{profile.hobbies} {profile.interests}",
        })
        
    context = {
        'profile_data' : profile_data
    }
    return render(request, 'user/user_profiles.html', context)
