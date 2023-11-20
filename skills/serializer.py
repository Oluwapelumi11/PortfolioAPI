from rest_framework import serializers
from .models import Skill, Certification


class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ()
    def to_representation(self,instance):
        data = super().to_representation(instance)
        skill_categories = {
            "Language": {},
            "Framework": {},
            "Databases": {},
            "Tools": {},
            "Other": {},
        }
        skill=[]
        for category in skill_categories.keys():
            skill= Skill.objects.filter(skill_type=category)
            j = 0
            for i in skill:
                skill_categories[category][str(j)]=str(i.name)
                j +=1
        data['skills'] = skill_categories
        return data
