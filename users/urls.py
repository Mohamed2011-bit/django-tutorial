
from django.urls import path
from users.views import register, home

urlpatterns = [
    path('',home),    
    path('',register)
]