from django.db import models


class Category(models.Model):
    category = models.CharField(blank=False, primary_key=True, max_length=30)
    description = models.CharField(blank=False, null=True, max_length=60)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name = 'Project Category'
        verbose_name_plural = 'Categories'