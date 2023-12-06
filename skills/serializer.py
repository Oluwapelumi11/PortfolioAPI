from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.Serializer):
    skills = serializers.DictField(child=serializers.ListField(child=serializers.CharField()))

    def to_representation(self, instance):
        return instance