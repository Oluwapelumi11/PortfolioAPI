from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Skill
from .serializer import SkillSerializer
from django.http import JsonResponse

class ListSkills(APIView):
    def get(self, request, *args, **kwargs):
        skills_by_category = self.get_skills_by_category()
        serializer = SkillSerializer(skills_by_category, many=True)
        return Response(serializer.data)


    def get_skills_by_category(request):
        skills_by_category = {
            "Language": set(),
            "Framework": set(),
            "Databases": set(),
            "Tools": set(),
            "Other": set(),
        }

        skills = Skill.objects.all()

        for skill in skills:
            skills_by_category[skill.skill_type].add(skill.name)

        result = [{"category": category, "skills": list(skills)} for category, skills in skills_by_category.items()]

        return result
