from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.LandingPage, name='landing_page'),
    path('login', auth_views.LoginView.as_view(template_name='login_page.html'), name="login_page"),
    path('logout', auth_views.LogoutView.as_view(template_name='login_page.html'), name="login_out"),
    path('login_validator', views.LoginUser, name='login_validator'),

    path('profile', views.ProfilePage, name='profile_page'),
    path('profile/update_info', views.UpdateUserProfile, name='update_info'),

   path('location', views.LocationMap, name='location_page'), 
   path('location/map', views.GetUsersLocations, name='location_map'), 

]