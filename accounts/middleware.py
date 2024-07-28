# middleware.py

from django.shortcuts import redirect
from django.urls import reverse
from .models import UserProfile

class ProfileCompletionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                if not profile.is_complete():  # Assuming `is_complete` is a method that checks if the profile is filled out
                    if request.path != reverse('accounts:update_profile'):
                        return redirect('accounts:update_profile')
            except UserProfile.DoesNotExist:
                pass
        return self.get_response(request)

