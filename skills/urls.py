from django.urls import path
from .api_view import ListSkills

urlpatterns = [
    path('',ListSkills.as_view())
]
