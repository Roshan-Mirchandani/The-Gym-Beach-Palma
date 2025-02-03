from django.urls import path
from . import views

urlpatterns = [
    path('<str:location>/', views.staff, name ='staff')
]