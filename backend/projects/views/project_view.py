from rest_framework import viewsets, permissions
from ..serializers import ProjectSerializer, ProjectDetailSerializer, ProjectBeneficiarySerializer, ProjectCollaboratorSerializer
from ..models import Project, ProjectCollaborator, ProjectBeneficiary


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ProjectDetailViewset(viewsets.ModelViewSet):
    serializer_class = ProjectDetailSerializer
    queryset = Project.objects.all()


class ProjectBeneficiaryViewset(viewsets.ModelViewSet):
    serializer_class = ProjectBeneficiarySerializer
    queryset = ProjectBeneficiary.objects.all()
    slug_field = 'project_id'
    slug_url_kwarg = 'project_id'

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data[self.slug_field] = self.kwargs[self.slug_url_kwarg]
        return request

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project=self.kwargs[self.slug_url_kwarg])
        return queryset


class ProjectCollaboratorViewset(viewsets.ModelViewSet):
    serializer_class = ProjectCollaboratorSerializer
    queryset = ProjectCollaborator.objects.all()
    slug_field = 'project_id'
    slug_url_kwarg = 'project_id'

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data[self.slug_field] = self.kwargs[self.slug_url_kwarg]
        return request

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project=self.kwargs[self.slug_url_kwarg])
        return queryset
