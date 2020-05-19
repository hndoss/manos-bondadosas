from django.db import models
from .task_category import TaskCategory
from .project import Project


class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=30)
    due = models.DateTimeField()
    description = models.CharField(blank=False, null=True, max_length=60)

    responsable = models.ForeignKey(
        'collaborators.Collaborator', on_delete=models.CASCADE)
    category = models.ForeignKey(TaskCategory, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name