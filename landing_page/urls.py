# landing_page/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('location/<str:location>/', views.gym_location, name='gym_location')
]
