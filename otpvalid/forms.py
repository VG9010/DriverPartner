from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Ride, Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Enter email-address", "class": "form-control"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Enter username", "class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"placeholder": "Enter password", "class": "form-control"}))
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={"placeholder": "Confirm password", "class": "form-control"}))
    
    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]

class RideSearchForm(forms.Form):
    pickup_location = forms.CharField(max_length=255, required=True)
    drop_location = forms.CharField(max_length=255, required=True)

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_location', 'dropoff_location', 'price', 'distance']  # Adjust fields as needed
        widgets = {
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
            'distance': forms.NumberInput(attrs={'placeholder': 'Enter Distance'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_photo']

class PublishRideForm(forms.Form):
    pickup_lat = forms.FloatField(label='Pickup Latitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Pickup Latitude'}))
    pickup_lng = forms.FloatField(label='Pickup Longitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Pickup Longitude'}))
    drop_lat = forms.FloatField(label='Drop Latitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Drop Latitude'}))
    drop_lng = forms.FloatField(label='Drop Longitude', widget=forms.NumberInput(attrs={'placeholder': 'Enter Drop Longitude'}))
    pickup_location = forms.CharField(label='Pickup Location', widget=forms.TextInput(attrs={'placeholder': 'Enter Pickup Location'}))
    drop_location = forms.CharField(label='Drop Location', widget=forms.TextInput(attrs={'placeholder': 'Enter Drop Location'}))
    pickup_time = forms.TimeField(label='Pickup Time', widget=forms.TimeInput(format='%H:%M'))
    drop_time = forms.TimeField(label='Drop Time', widget=forms.TimeInput(format='%H:%M'))
    price = forms.DecimalField(label='Price', widget=forms.NumberInput(attrs={'placeholder': 'Enter Price'}))

from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['publisher_name', 'vehicle_name', 'pickup_location',  'pickup_lat', 'pickup_lng', 'dropoff_lat', 'dropoff_lng', 'price']
        widgets = {
            'distance': forms.NumberInput(attrs={'placeholder': 'Enter Distance'}),
            'pickup_lat': forms.NumberInput(attrs={'placeholder': 'Enter Pickup Latitude'}),
            'pickup_lng': forms.NumberInput(attrs={'placeholder': 'Enter Pickup Longitude'}),
            'dropoff_lat': forms.NumberInput(attrs={'placeholder': 'Enter Drop Latitude'}),
            'dropoff_lng': forms.NumberInput(attrs={'placeholder': 'Enter Drop Longitude'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
        }
        
class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_location', 'drop_location', 'price']  # Remove or fix 'dropoff_location' and 'distance'
        widgets = {
            'price': forms.NumberInput(attrs={'placeholder': 'Enter Price'}),
        }

from django import forms

class YourFormClass(forms.Form):
    {
        
    }
    

from django import forms
from .models import Ride

class FindRideForm(forms.Form):
    pickup_location = forms.CharField(max_length=100)
    drop_location = forms.CharField(max_length=100)
    # Add other fields if necessary
