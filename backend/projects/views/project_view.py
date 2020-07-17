from rest_framework import viewsets, permissions
from ..serializers import ProjectSerializer, ProjectDetailSerializer
from ..models import Project


class ProjectViewset(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ProjectDetailSerializer
        return self.serializer_class