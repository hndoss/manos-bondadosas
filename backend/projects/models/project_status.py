from django.db import models


class ProjectStatus(models.Model):
    status = models.CharField(blank=False, primary_key=True, max_length=30)
    description = models.CharField(blank=False, null=True, max_length=60)

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Project Status'
        verbose_name_plural = 'Statuses'