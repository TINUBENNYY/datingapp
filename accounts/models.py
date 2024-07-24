from django.contrib.auth.models import AbstractUser, User
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default= 'M')
    phone = models.CharField(max_length=10, blank=True, null=True)

class UserProfile(models.Model):
    id = models.BigAutoField(primary_key= True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)  
    hobbies = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    smoking_habits = models.CharField(max_length=100)
    drinking_habits = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    profile_pic = models.ImageField(upload_to='profile_pics/')
    multiple_images = models.ImageField(upload_to='user_images/', blank=True, null=True)
    short_reel =models.FileField(upload_to='user_reels/', blank=True, null=True)

    class Meta:
        db_table = 'user_profile'

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
    employment_type = models.CharField(max_length=20 , choices=EMPLOYMENT_CHOICES)
    company_name = models.CharField(max_length=100 , blank=True, null=True)
    designation = models.CharField(max_length=100 ,  blank=True, null=True) 
    location = models.CharField(max_length=100 , blank=True, null=True)
    job_title = models.CharField(max_length=100 , blank=True, null=True)
    expertise_level = models.CharField(max_length=20 , choices=EXPERTISE_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s Employment Profile"