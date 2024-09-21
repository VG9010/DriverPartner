from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .views import find_your_ride,signup,available_rides

urlpatterns = [
    path("", views.index, name="index"),
    # path('', find_ride, name='find_ride'),
    path('signup/', signup, name='Signup'),
    path("register", views.signup, name="register"),
    path("verify-token/<slug:username>/", views.verify_email, name="verify_token"),
    path("resend-otp", views.resend_otp, name="resend-otp"),
    path("login", views.signin, name="signin"),
    path('find-your-ride/', views.find_your_ride, name='find_your_ride'),  # Find your ride page
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Login page
    
    path('profile/', views.profile_view, name='profile'),  # Profile page
    path('about/', views.about_view, name='about'),        # About page
    path('account/', views.account_view, name='account'),  # Account page
    path('about-us/',views.about_us_view,name='about_us'),
    
    
    path('publish-ride/', views.publish_ride, name='publish_ride'),
    path('ride-success/', views.ride_success, name='ride_success'),
    
    path('publish-ride/', views.publish_ride, name='publish_ride'),
    path('available-rides/', views.available_rides, name='available_rides'),
    path('find-your-ride/', find_your_ride, name='find_your_ride'),
    
    path('publish-ride/', views.publish_ride, name='publish_ride'),
    path('available-rides/', views.available_rides, name='available_rides'),
    path('rides/publish/', views.publish_ride, name='publish_ride'),
    path('rides/available/', views.available_rides, name='available_rides'),
    #path('available-rides/<str:pickup_location>/<str:drop_location>/', views.available_rides, name='available-rides'),
    
    # path('find-your-ride/', views.find_your_ride, name='find_your_ride'),
    # path('search/', views.search_redirect, name='search_redirect'),
    # path('find_ride/', views.find_ride, name='find_ride'),
]
