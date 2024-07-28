from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    hobbies = models.CharField(max_length=100, blank=True, null=True)
    interest = models.CharField(max_length=100, blank=True, null=True)
    smoking_habits = models.CharField(max_length=100, blank=True, null=True)
    drinking_habits = models.CharField(max_length=100, blank=True, null=True)
    qualification = models.CharField(max_length=100, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    multiple_images = models.ImageField(upload_to='user_images/', blank=True, null=True)
    short_reel = models.FileField(upload_to='user_reels/', blank=True, null=True)
    first_time_login = models.BooleanField(default=True)

    def is_complete(self):
        required_fields = [self.age, self.dob, self.hobbies, self.interest]
        return all(field is not None for field in required_fields)

class EmploymentProfile(models.Model):
    EMPLOYMENT_CHOICES = (
        ('employee', 'Employee/Employer'),
        ('job_seeker', 'Job Seeker'),
    )
    EXPERTISE_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('expert', 'Expert'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    job_title = models.CharField(max_length=100, blank=True, null=True)
    expertise_level = models.CharField(max_length=20, choices=EXPERTISE_CHOICES)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

class MatchPreference(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    seeking = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    age_min = models.IntegerField(blank=True, null=True)
    age_max = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"Preference of {self.user.username}"