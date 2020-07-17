from django.contrib import admin
from import_export import resources
from .models import Beneficiary, Collaborator
from import_export.admin import ImportExportModelAdmin


class CollaboratorResource(resources.ModelResource):
    class Meta:
        model = Collaborator


class CollaboratorAdmin(ImportExportModelAdmin):
    resource_class = CollaboratorResource


class BeneficiaryResource(resources.ModelResource):
    class Meta:
        model = Beneficiary


class BeneficiaryAdmin(ImportExportModelAdmin):
    resource_class = BeneficiaryResource


admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Collaborator, CollaboratorAdmin)
