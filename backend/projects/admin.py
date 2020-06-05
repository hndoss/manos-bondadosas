from django.contrib import admin
from .models import Project, Category, Status


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', )
    filter_horizontal = ('collaborators', 'beneficiaries', )


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(Status)
