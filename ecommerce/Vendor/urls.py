from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.VendorsList.as_view(), name="vendor-vendors"),
    path('join', views.JoinAsVendor.as_view(), name="vendor-join"),
    path('register', views.RegisterAsVendor.as_view(), name="vendor-join-register"),
    path('resend-email/<int:id>', views.ResendRegistrationEmail.as_view(), name="vendor-resend-email")
]