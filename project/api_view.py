from rest_framework.generics import ListAPIView

from .serializer import ProjectSerializer
from .models import Project

class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
