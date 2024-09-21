

from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        read_only_fields = ('date_published',)
        fields = ['publisher_name', 'vehicle_name', 'pickup_location',  'price']
        widgets = {
            'pickup_location': forms.TextInput(attrs={'id': 'pickup'}),
            
        }


from django import forms
from .models import Ride

class RideForm(forms.ModelForm):
    class Meta:
        model = Ride
        read_only_fields = ('date_published',)
        fields = ['publisher_name', 'vehicle_name', 'pickup_location', 'pickup_time', 'price', 'ride_date', 'ride_time', 'passengers']
        widgets = {
            'pickup_location': forms.TextInput(attrs={'id': 'pickup'}),
        }
        
from django import forms
from .models import Ride

class RidePublishForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ['pickup_location', 'drop_location', 'pickup_time', 'drop_time', 'price', 'ride_date', 'ride_time', 'passengers']
        
