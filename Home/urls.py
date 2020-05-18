from django.urls import path

from Home import views

urlpatterns = [
    path("register-farmer/", views.FarmerRegistrationPage, name="register_farmer"),
    path("register-buyer/", views.BuyerRegistrationPage, name="register_buyer"),
    path("portal-login/", views.PortalLogin, name="portal_login"),
    path("portal-profile/", views.PortalProfile, name="portal_profile"),
    path("f-profile/", views.FarmerProfile, name="farmer_profile"),
    path("b-profile/", views.BuyerProfile, name="buyer_profile"),
]
