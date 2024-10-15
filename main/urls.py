# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing'),
    path('register/', views.register, name='register'),
    path('program/', views.program, name='program'),
    path('waitlist/', views.waitlist, name='waitlist'), 
    path('thank_you/', views.thank_you, name='thank_you'),
    path('thank_you_waitlist/', views.thank_you_waitlist, name='thank_you_waitlist'),
]
