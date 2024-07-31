from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from accounts.models import UserProfile, EmploymentProfile, MatchPreference, User

class IndexView(View):
    def get(self, request):
        profiles = UserProfile.objects.all()
        return render(request, 'user/index.html', {'profiles': profiles})
    
class UserProfileDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user/user_profile_details.html'
    context_object_name = 'profile_user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['user_profile'] = UserProfile.objects.get(user=user)
        context['employment_profile'] = EmploymentProfile.objects.filter(user=user).first()
        context['match_preference'] = MatchPreference.objects.filter(user=user).first()
        return context




   