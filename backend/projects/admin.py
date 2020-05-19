from django.contrib import admin
from .models import Project, ProjectCategory, ProjectStatus


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    filter_horizontal = ('collaborators',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory)
admin.site.register(ProjectStatus)
