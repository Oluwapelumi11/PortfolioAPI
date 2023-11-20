from django.db import models
# Create your models here.


class Project(models.Model):
    title = models.CharField(("Title"), max_length=50)
    skills = models.ManyToManyField("skills.Skill", verbose_name=("Skills"))
    description = models.TextField(("Description"))
    live = models.BooleanField(("Live"))
    featured = models.BooleanField(("Featured"))
    image = models.ImageField(("Image"), upload_to="projects/", height_field=None, width_field=None, max_length=None)
    live_url = models.URLField(("Url"), max_length=200,null=True, blank=True)
    github_url = models.URLField(("Github Link"), max_length=200)
    small_project = models.BooleanField(("Small project"))
    data_analysis = models.BooleanField(("Data Analysis"), null=True, blank=True)
    

    def __str__(self):
        return self.title
    