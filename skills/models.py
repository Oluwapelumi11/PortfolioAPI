from django.db import models

# Create your models here.

class SkillManager(models.Manager):
    def get_skills_by_category(self):
        skills_by_category = {
            "Language": set(),
            "Framework": set(),
            "Databases": set(),
            "Tools": set(),
            "Other": set(),
        }

        skills = self.all()

        for skill in skills:
            skills_by_category[skill.skill_type].add(skill.name)

        return {category: list(skills) for category, skills in skills_by_category.items()}


class Certification(models.Model):
    title = models.CharField(("Title"), max_length=50)
    institution = models.CharField(("Institute"), max_length=50)
    image = models.ImageField(("Image"), upload_to='certificates/', height_field=None, width_field=None, max_length=None)
    file = models.FileField(("Upload File"), upload_to="files/", max_length=100)

class Skill(models.Model):
    skill_choice_type = (
        ("Language","Language"),
        ("Framework", "Framework"),
        ("Databases", "Databases"),
        ("Tools", "Tools"),
        ("Other", "Other"),
    )
    name =models.CharField(("Name"), max_length=50)
    skill_type = models.CharField( max_length=50, choices=skill_choice_type, 
    default="Language")
    certificates = models.ForeignKey(Certification, verbose_name=("Certificates"), on_delete=models.CASCADE,null=True, blank=True)



    def __str__(self):
        return self.name



