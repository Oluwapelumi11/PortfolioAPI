from .models import Skill, Certification
from .serializer import SkillSerializer, CertificationSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView


class SkillList(RetrieveAPIView):
    queryset= Skill.objects.all()
    serializer_class=SkillSerializer
    lookup_field = 'pk'


class CertificateList(ListAPIView):
    queryset= Certification.objects.all()
    serializer_class=CertificationSerializer