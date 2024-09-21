from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import OtpToken
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect,HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RideSearchForm
from .models import Ride
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import views as auth_views
from django.http import HttpResponseForbidden,HttpResponseBadRequest
from django.shortcuts import render
from .forms import YourFormClass
from django.http import HttpResponse
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
import json





def index(request):
    return render(request, "index.html")

@csrf_exempt  # Use this decorator if you don't have CSRF token in AJAX requests, though not recommended
def save_profile(request):
    if request.method == 'POST':
        
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        country = request.POST.get('country')
        language = request.POST.get('language')
        email = request.POST.get('email')

        
        if 'profile_picture' in request.FILES:
            profile_picture = request.FILES['profile_picture']
            fs = FileSystemStorage()
            filename = fs.save(profile_picture.name, profile_picture)
            uploaded_file_url = fs.url(filename)
            # You can save `uploaded_file_url` in the user profile or return it

       
        user = request.user
        user.name = name
        user.dob = dob
        user.country = country
        user.language = language
        user.email = email

        # Optionally save the uploaded image URL to the user profile
        # user.profile_picture = uploaded_file_url
        user.save()

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import RideSearchForm
from .models import Ride

@login_required
def find_your_ride(request):
    if request.method == 'POST':
        form = RideSearchForm(request.POST)
        if form.is_valid():
            pickup_location = form.cleaned_data['pickup_location']
            drop_location = form.cleaned_data['drop_location']

            # Search for available rides
            rides = Ride.objects.filter(pickup_location__icontains=pickup_location,
                                        drop_location__icontains=drop_location)
            
            return render(request, 'find_your_ride.html', {'form': form, 'rides': rides})

    else:
        form = RideSearchForm()
    
    return render(request, 'find_your_ride.html', {'form': form})




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after signup
            return redirect('home')  # Redirect to homepage or other page after signup
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def profile_view(request):
    return render(request, 'profile.html')  # Render the profile page

def about_view(request):
    return render(request, 'about.html')  # Render the about page

def account_view(request):
    return render(request, 'account.html')  # Render the account page

def about_us_view(request):
    return render(request, 'about-us.html') 



#publish ride 
from .forms import RideForm
from .forms import PublishRideForm

@login_required
def publish_ride(request):
    if request.method == 'POST':
        form = RideForm(request.POST)
        if form.is_valid():
            # Save the ride with the logged-in user
            ride = form.save(commit=False)
            ride.user = request.user
            ride.save()
            # Provide a success message
            messages.success(request, 'Your ride has been published successfully!')
            return redirect('ride_success')  # Redirect to a success page or another relevant page
        else:
            messages.error(request, 'There was an error with your form. Please correct the errors below.')
    else:
        form = PublishRideForm()

    return render(request, 'publish-ride.html', {'form': form})


@login_required
def ride_success(request):
    return render(request, 'ride_success.html')

def available_rides(request):
    pickup_location = request.GET.get('pickup_location')
    drop_location = request.GET.get('drop_location')

    if pickup_location and drop_location:
        rides = Ride.objects.filter(pickup_location=pickup_location, drop_location=drop_location)
    else:
        rides = Ride.objects.all()  # Show all rides if no filter is applied

    return render(request, 'available_rides.html', {'rides': rides})


#*********************publish ride after******************
from django.shortcuts import render, redirect
from .forms import RideForm

# Example model for storing rides
from .models import Ride

from django.shortcuts import render, redirect
from .models import Ride  # Assuming you have a Ride model to store the ride details

def publish_ride(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You need to be logged in to publish a ride.")

        # Fetch form data
        pickup_location = request.POST.get('pickup_location')
        drop_location = request.POST.get('drop_location')
        pickup_time = request.POST.get('pickup_time')
        drop_time = request.POST.get('drop_time')
        price = request.POST.get('price')
        
        form = RideForm(request.POST)
        if drop_time:  # Check if drop_time is not empty
            Ride.objects.create(
                user_id=request.user.id,
                pickup_location=pickup_location,
                drop_location=drop_location,
                pickup_time=pickup_time,
                drop_time=drop_time,
                price=price
            )
            return redirect('available_rides')
        
        # Redirect to the available rides page after successful submission
        return redirect('available_rides.html')

    return render(request, 'publish-ride.html')
from django.shortcuts import render, redirect
from .models import Ride

def publish_ride(request):
    if request.method == 'POST':
        pickup_location = request.POST.get('pickup-location')
        drop_location = request.POST.get('drop-location')
        pickup_time = request.POST.get('pickup-time')
        drop_time = request.POST.get('drop-time')
        price = request.POST.get('price')

        # Create a new Ride object and save it to the database
        new_ride = Ride(
            pickup_location=pickup_location,
            drop_location=drop_location,
            pickup_time=pickup_time,
            drop_time=drop_time,
            price=price
        )
        new_ride.save()

        # After saving, redirect to the available rides page
        return redirect('available_rides')  # Make sure you have this URL in urls.py
    
    return render(request, 'publish-ride.html')

def available_rides(request):
    # Fetch all available rides from the database
    available_rides = Ride.objects.all()

    # Render the available rides template with the available rides data
    return render(request, 'available_rides.html', {'available_rides': available_rides})

from django.shortcuts import render
from .models import Ride

def available_rides(request):
    rides = Ride.objects.all()  # Fetch all available rides from the database
    return render(request, 'available-rides.html', {'rides': rides})

def find_your_ride(request):
    if request.method == 'POST':
        form = YourFormClass(request.POST)
        if form.is_valid():
            # Handle form processing
            pass
    else:
        form = YourFormClass()
    return render(request, 'find_your_ride.html', {'form': form})


# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Ride
from .forms import FindRideForm

@login_required
def find_your_ride(request):
    if request.method == 'POST':
        form = FindRideForm(request.POST)
        if form.is_valid():
            # Get user input locations
            pickup_location = form.cleaned_data['pickup_location']
            drop_location = form.cleaned_data['drop_location']
            
            # Redirect to the available rides page with locations as query params
            return redirect('available_rides', pickup_location=pickup_location, drop_location=drop_location)
    else:
        form = FindRideForm()

    return render(request, 'available-rides.html', {'form': form})

@login_required
def available_rides(request, pickup_location, drop_location):
    # Fetch available rides that match user’s input locations
    rides = Ride.objects.filter(pickup_location=pickup_location, drop_location=drop_location)
    return render(request, 'available-rides.html', {'rides': rides})


# your_app/views.py
from django.shortcuts import render

def available_rides(request, pickup_location, drop_location):
    # Debug print to check if parameters are received
    print(f"Pickup Location: {pickup_location}, Drop Location: {drop_location}")
    
    # Fetch or display the rides based on the parameters
    context = {
        'pickup_location': pickup_location,
        'drop_location': drop_location,
    }
    return render(request, 'available-rides.html', context)









#************************profile******************************

# views.py
from django.shortcuts import render, redirect
from .forms import ProfileUpdateForm

def about(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('about')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    
    return render(request, 'yourapp/about.html', {'form': form})

def index(request):
    print(f"User object: {request.user}")
    return render(request, "index.html")










#**********************************verify email code********************************************************
def signup(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! An OTP was sent to your Email")
            return redirect(verify_email, username=request.POST['username'])
    context = {"form": form}
    return render(request, "signup.html", context)




def verify_email(request, username):
    user = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
    
    
    if request.method == 'POST':
        # valid token
        if user_otp.otp_code == request.POST['otp_code']:
            
            # checking for expired token
            if user_otp.otp_expires_at > timezone.now():
                user.is_active=True
                user.save()
                messages.success(request, "Account activated successfully!! You can Login.")
                return redirect("signin")
            
            # expired token
            else:
                messages.warning(request, "The OTP has expired, get a new OTP!")
                return redirect("verify_email", username=user.username)
        
        
        # invalid otp code
        else:
            messages.warning(request, "Invalid OTP entered, enter a valid OTP!")
        
    context = {}
    return render(request, 'verify_token.html', context)


def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST["otp_email"]
        
        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            
            # email variables
            subject="Email Verification"
            message = f"""
                                Hi {user.username}, here is your OTP {otp.otp_code} 
                                it expires in 5 minute, use the url below to redirect back to the website
                                http://127.0.0.1:8000/verify-token/{user.username}
                                
                                """
            sender = "gitevaibhav9010@gmail.com"
            receiver = [user.email, ]
        
        
            # send email
            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False,
                )
            
            messages.success(request, "A new OTP has been sent to your email-address")
            return redirect("verify-token", username=user.username)

        else:
            messages.warning(request, "This email dosen't exist in the database")
            return redirect("resend")
        
           
    context = {}
    return render(request, "resend.html", context)




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:    
            login(request, user)
            messages.success(request, f"Hi {request.user.username}, you are now logged-in")
            return redirect("index")
        
        else:
            messages.warning(request, "Invalid credentials")
            return redirect("signin")
        
    return render(request, "login.html")
    