from django.contrib import admin
from .models import Collaborator
from django.apps import apps


class CollaboratorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', )


admin.site.register(Collaborator, CollaboratorAdmin)
