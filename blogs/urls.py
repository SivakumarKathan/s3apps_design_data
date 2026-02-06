from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.stories, name='stories'),
    path('services/', views.services, name='services'),
]