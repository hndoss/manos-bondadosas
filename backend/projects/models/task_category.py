from django.db import models


class TaskCategory(models.Model):
    category = models.CharField(primary_key=True, max_length=30)
    description = models.CharField(blank=False, null=True, max_length=60)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Task Category'
        verbose_name_plural = 'Categories'