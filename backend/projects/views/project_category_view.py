from rest_framework import viewsets, permissions
from ..serializers import ProjectCategorySerializer
from ..models import ProjectCategory


class ProjectCategoryView(viewsets.ModelViewSet):
    serializer_class = ProjectCategorySerializer
    queryset = ProjectCategory.objects.all()
