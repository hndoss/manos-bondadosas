from django.db import models
from .task_category import TaskCategory
from .project import Project


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=30)
    due = models.DateTimeField(blank=True, null=True)
    description = models.CharField(blank=False, null=True, max_length=60)
    order = models.IntegerField(blank=False, null=False)
    responsable = models.ForeignKey(
        'collaborators.Collaborator', on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        TaskCategory, on_delete=models.CASCADE, blank=True, null=True)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
