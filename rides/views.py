# rides/views.py

from django.shortcuts import render, redirect
from .forms import RideForm
from .models import Ride
from geopy. distance import geodesic
from .forms import RidePublishForm


def add_ride(request):
    if request.method == "POST":
        form = RideForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.pickup_lat = request.POST.get('pickup_lat')
            ride.pickup_lng = request.POST.get('pickup_lng')
            ride.dropoff_lat = request.POST.get('dropoff_lat')
            ride.dropoff_lng = request.POST.get('dropoff_lng')

            # Calculate the distance using geopy
            pickup_point = (ride.pickup_lat, ride.pickup_lng)
            dropoff_point = (ride.dropoff_lat, ride.dropoff_lng)
            ride.distance = geodesic(pickup_point, dropoff_point).km

            ride.save()
            return redirect('ride_list')
    else:
        form = RideForm()
    return render(request, 'rides/add_ride.html', {'form': form})

def ride_list(request):
    rides = Ride.objects.all()
    return render(request, 'rides/ride_list.html', {'rides': rides})


# views.py
from django.shortcuts import render, redirect
from .models import Ride
from .forms import RidePublishForm
from django.contrib.auth.decorators import login_required

@login_required
def publish_ride(request):
    if request.method == 'POST':
        form = RidePublishForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.user = request.user
            ride.save()
            return redirect('ride_detail', pk=ride.pk)
    else:
        form = RideForm()
    return render(request, 'publish-ride.html', {'form': form})

def ride_detail(request, pk):
    ride = Ride.objects.get(pk=pk)
    return render(request, 'ride_detail.html', {'ride': ride})


from django.db.models import Q

def available_rides(request):
    query = request.GET.get('q')
    if query:
        rides = Ride.objects.filter(
            Q(start_location__icontains=query) | Q(end_location__icontains=query)
        )
    else:
        rides = Ride.objects.all()
    return render(request, 'available_rides.html', {'rides': rides})


from django.shortcuts import render
from .models import Ride  # Assuming Ride is your model

def available_rides(request):
    rides = Ride.objects.all()  # Fetch all rides from the database
    context = {
        'rides': rides  # Pass the rides queryset to the template
    }
    return render(request, 'rides/available_rides.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Ride

def ride_detail(request, ride_id):
    ride = get_object_or_404(Ride, pk=ride_id)
    context = {
        'ride': ride
    }
    return render(request, 'rides/ride_detail.html', context)




from django.shortcuts import render, redirect
from .forms import RideForm

def create_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # replace with your success URL
    else:
        form = RideForm()
    return render(request, 'create_ride.html', {'form': form})


def find_your_ride(request):
    if request.method == 'POST':
        form = RidePublishForm(request.POST)
        if form.is_valid():
            pickup_location = form.cleaned_data['pickup_location']
            # Continue with your logic
        else:
            # Handle form errors
            print(form.errors)  # Debugging line to see what went wrong
    else:
        form = RidePublishForm()
    return render(request, 'available-rides.html', {'form': form})


def find_your_ride(request):
    if request.method == 'POST':
        form = RidePublishForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)  # Debugging line to check cleaned_data
            pickup_location = form.cleaned_data.get('pickup_location')
            if pickup_location is None:
                print('pickup_location is not in cleaned_data')
            # Continue with your logic
        else:
            print(form.errors)  # Debugging line to see what went wrong
    else:
        form = RidePublishForm()
    return render(request, 'available-rides.html', {'form': form})


from django.shortcuts import render
from .models import Ride

from django.shortcuts import render
from .models import Ride

def available_rides(request):
    rides = Ride.objects.select_related('publisher').all()  # Select related for better performance
    return render(request, 'available-rides.html', {'rides': rides})
