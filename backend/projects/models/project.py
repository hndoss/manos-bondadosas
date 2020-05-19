from django.db import models
from .project_status import ProjectStatus
from .project_category import ProjectCategory


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=60)
    description = models.CharField(blank=False, null=True, max_length=120)
    direction = models.CharField(blank=False, null=True, max_length=120)
    collaborators = models.ManyToManyField(
        'collaborators.Collaborator', blank=True)

    status = models.ForeignKey(ProjectStatus, on_delete=models.CASCADE)
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name