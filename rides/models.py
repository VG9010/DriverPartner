from django.db import models
from django.conf import settings

class Ride(models.Model):
    publisher_name = models.CharField(max_length=100)
    vehicle_name = models.CharField(max_length=100)
    pickup_location = models.CharField(max_length=255) 
    drop_location = models.CharField(max_length=255,  null=True)
    pickup_time = models.TimeField()
    drop_time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ride_date = models.DateField()
    ride_time = models.TimeField()
    passengers = models.IntegerField()
    
    dropoff_location = models.CharField(max_length=255)  # Corrected field name
    distance = models.DecimalField(max_digits=10, decimal_places=2)  # Added field
    date_published = models.DateTimeField(auto_now_add=True, editable=False)
    def __str__(self):
        return f"Ride by {self.publisher_name} from {self.pickup_location} to {self.dropoff_location}"

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides_profile')
    profile_photo = models.ImageField(upload_to='profiles/')
    experience = models.IntegerField(default=0)
    rating = models.FloatField(default=4.5)