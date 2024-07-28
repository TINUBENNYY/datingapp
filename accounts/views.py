
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, CreateView
from .models import MatchPreference, UserProfile, EmploymentProfile
from .forms import LoginFrom, MatchPreferenceForm, UserCreationForm, UserProfileForm, EmploymentProfileForm
from django.views.generic import View, TemplateView
from django.core.exceptions import PermissionDenied



# Create your views here.


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            # user.set_password(form.cleaned_data['password'])
            login(request, user)
            UserProfile.objects.create(user=user)
            return redirect('login') #Redirect to a success page
        else:
            form = UserCreationForm()
            return render(request, 'accounts/register.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = LoginFrom()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = LoginFrom(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'userprofile'):
                    return redirect('/')  # User has a profile, redirect to home
                else:
                    # Create a UserProfile for the user
                    UserProfile.objects.create(user=user)
                    return redirect('accounts:update_profile')  # Redirect to profile setup
        return render(request, 'accounts/login.html', {'form': form})
    
class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('accounts:employment_registration')

    def get_object(self, queryset=None):
        # Get or create a UserProfile for the current user
        obj, created = UserProfile.objects.get_or_create(user=self.request.user)
        return obj
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    def get_initial(self):
        # Pre-fill the form with existing data if available
        initial = super().get_initial()
        user_profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        if not created:
            for field in self.form_class.Meta.fields:
                initial[field] = getattr(user_profile, field)
        return initial
    def dispatch(self, request, *args, **kwargs):
        try:
            self.request.user.userprofile
        except UserProfile.DoesNotExist:
            raise PermissionDenied("You must create a profile first.")
        return super().dispatch(request, *args, **kwargs)
    
   
class EmploymentRegistrationView(LoginRequiredMixin, CreateView):
    model = EmploymentProfile
    form_class = EmploymentProfileForm
    template_name = 'accounts/employment_registration.html'
    success_url = reverse_lazy('accounts:first_time_choice')

    def dispatch(self, *args, **kwargs):
        user_profile = UserProfile.objects.filter(user=self.request.user).first()
        if not user_profile:
            return redirect('user_profile_creation_url')  # Redirect to user profile creation page
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class FirstTimeChoiceView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/first_time_choice.html'

    def post(self, request, *args, **kwargs):
        choice = request.POST.get('choice')
        request.user.userprofile.first_time_login = False
        request.user.userprofile.save()
        if choice == 'short_term':
            return redirect('user:index') 
        elif choice == 'long_term':
            return redirect('matrimony_home')  # Replace with your matrimony site's home page URL name
        return render(request, self.template_name)

class MatchPreferenceCreateView(LoginRequiredMixin, CreateView):
    model = MatchPreference
    form_class = MatchPreferenceForm
    template_name = 'accounts/match_preference.html'
    success_url = reverse_lazy('user:index')  # Replace with your actual success URL

    def get_object(self, queryset=None):
        # Ensure the user can only update their own preferences
        return MatchPreference.objects.get(user=self.request.user)
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
def logout_user(request):
    logout(request)
    return redirect('/')
    
 