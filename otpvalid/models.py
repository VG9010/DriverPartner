from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission,User
from django.conf import settings
import secrets
import uuid
from datetime import date
from django.utils import timezone
from datetime import time

# Custom User Model
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.email

# OTP Token Model
class OtpToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="otps")
    otp_code = models.CharField(max_length=6, default=secrets.token_hex(3))
    otp_created_at = models.DateTimeField(auto_now_add=True)
    otp_expires_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username

# Ride Model
# class Ride(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     pickup_location = models.CharField(max_length=255)
#     drop_location = models.CharField(max_length=255)
#     date = models.DateTimeField()
#     verification_code = models.CharField(max_length=6, default=uuid.uuid4().hex[:6], blank=True)
#     email_verified = models.BooleanField(default=False)
    
#     def __str__(self):
#         return f"{self.pickup_location} to {self.drop_location} on {self.date}"

from django.conf import settings
from django.db import models
from datetime import date, time

class Ride(models.Model):
    ride_user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    # ride_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_set')
    pickup_location = models.CharField(max_length=255, blank=True, null=True)
    drop_location = models.CharField(max_length=255,  null=True)
    drop_location = models.CharField(max_length=255)
    pickup_time = models.TimeField(default=time(9, 0))  # Adding pickup_time
    drop_time = models.DateTimeField(null=True)    
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)  # Adding price
    ride_date = models.DateField(default=date.today)
    ride_time = models.TimeField(default=time(12, 0))
    passengers = models.IntegerField(default=1)
    date_published = models.DateTimeField(default=timezone.now)
    dropoff_location = models.CharField(max_length=255)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    pickup_lat = models.DecimalField(max_digits=10, decimal_places=8)
    publisher_name = models.CharField(max_length=255)
    pickup_lng = models.DecimalField(max_digits=11, decimal_places=8)
    vehicle_name = models.CharField(max_length=255)
    dropoff_lat = models.DecimalField(max_digits=10, decimal_places=8)
    dropoff_lng = models.DecimalField(max_digits=11, decimal_places=8)
    date_published = models.DateTimeField(auto_now_add=True, editable=False)
    distance = models.IntegerField(default=0)
    dropoff_lat = models.FloatField(default=0.0)
    dropoff_lng = models.FloatField(default=0.0)
    dropoff_location = models.CharField(max_length=255, default='Unknown')
    pickup_lat = models.FloatField(default=0.0)
    publisher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='published_rides')
    ride_user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rider_rides')
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    pickup_time = models.TimeField()
    drop_time = models.TimeField()
    
    def __str__(self):
        return f'Ride from {self.pickup_location} to {self.drop_location} on {self.ride_date} at {self.ride_time}'

    def __str__(self):
        return f"Ride from {self.pickup_location} to {self.drop_location} by {self.user.username}"


# class Ride(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     pickup_location = models.CharField(max_length=255)
#     drop_location = models.CharField(max_length=255)
#     ride_time = models.DateTimeField()
    
#     def __str__(self):
#         return f"Ride from {self.pickup_location} to {self.drop_location}"

# models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(default='default_avatar.png', upload_to='profile_pics')
    profile_photo = models.ImageField(upload_to='profile_photos/', default='path/to/default/image.jpg')
    
    def __str__(self):
        return f'{self.user.username}'

