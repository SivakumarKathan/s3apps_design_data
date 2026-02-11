from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name='home'),
    path('stories/', views.stories, name='stories'),
    path('stories/<int:post_id>/', views.story_detail, name='story_detail'),
    path('services/', views.services, name='services'),
]