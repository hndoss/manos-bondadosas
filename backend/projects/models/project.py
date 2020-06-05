from django.db import models
from .status import Status
from .category import Category


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=60)
    description = models.CharField(blank=False, null=True, max_length=120)
    direction = models.CharField(blank=False, null=True, max_length=120)
    collaborators = models.ManyToManyField(
        'people.Collaborator', related_name='projects', blank=True)
    beneficiaries = models.ManyToManyField(
        'people.Beneficiary', through='ProjectBeneficiary', related_name='projects', blank=True)
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="projects")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name


class ProjectBeneficiary(models.Model):
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE)
    beneficiary_id = models.ForeignKey(
        'people.Beneficiary', on_delete=models.CASCADE)
