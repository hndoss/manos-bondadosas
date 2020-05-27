from django.db import models
from .status import Status
from .category import Category


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=60)
    description = models.CharField(blank=False, null=True, max_length=120)
    direction = models.CharField(blank=False, null=True, max_length=120)
    collaborators = models.ManyToManyField(
        'collaborators.Collaborator', blank=True)
    beneficiaries = models.ManyToManyField(
        'beneficiaries.Beneficiary', blank=True)

    # default related_name = project_set
    status = models.ForeignKey(
        Status, on_delete=models.CASCADE, related_name="projects")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="projects")

    # tasks =  models.ForeignKey(
    #     ProjectTask, on_delete=models.CASCADE, related_name="projects")

    def __str__(self):
        return self.name
