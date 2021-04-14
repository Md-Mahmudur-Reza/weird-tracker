from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

]
