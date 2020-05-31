from rest_framework import viewsets, permissions
from ..serializers import ProjectSerializer
from collaborators.serializers import CollaboratorSerializer
from beneficiaries.serializers import BeneficiarySerializer
from beneficiaries.models import Beneficiary
from collaborators.models import Collaborator
from ..models import Project


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectCollaboratorViewset(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()
    slug_field = 'project'
    slug_url_kwarg = 'project_id'

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data[self.slug_field] = self.kwargs[self.slug_url_kwarg]
        return request

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project=self.kwargs[self.slug_url_kwarg])
        return queryset


class ProjectBeneficiaryViewset(viewsets.ModelViewSet):
    serializer_class = BeneficiarySerializer
    queryset = Beneficiary.objects.all()
    slug_field = 'project'
    slug_url_kwarg = 'project_id'

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data[self.slug_field] = self.kwargs[self.slug_url_kwarg]
        return request

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project=self.kwargs[self.slug_url_kwarg])
        return queryset
