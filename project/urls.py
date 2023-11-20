from . import api_view 
from django.urls import path 

urlpatterns = [
    path('', api_view.ProjectList.as_view()),
]
