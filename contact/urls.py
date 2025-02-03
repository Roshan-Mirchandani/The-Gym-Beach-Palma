from django.urls import path
from . import views 

urlpatterns = [
    path('', views.contact, name = 'contact'),
    path('<str:location>/', views.contact, name = 'contact_with_location')
    
]