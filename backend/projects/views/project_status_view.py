from rest_framework import viewsets, permissions
from ..serializers import ProjectStatusSerializer
from ..models import ProjectStatus


class ProjectStatusView(viewsets.ModelViewSet):
    serializer_class = ProjectStatusSerializer
    queryset = ProjectStatus.objects.all()
