from django.urls import path
from . import views

urlpatterns = [
    path('<str:location>/', views.home_view, name='home'),
]
#