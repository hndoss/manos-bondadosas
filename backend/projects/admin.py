from django.contrib import admin
from .models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    filter_horizontal = ('collaborators',)


admin.site.register(Project, ProjectAdmin)
