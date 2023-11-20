from django.urls import path
from .api_view import SkillList,CertificateList

urlpatterns = [
    path('<int:pk>/', SkillList.as_view()),
    path('certificates', CertificateList.as_view())
]
