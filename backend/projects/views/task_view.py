from rest_framework import viewsets, permissions
from ..serializers import TaskSerializer
from ..models import Task


class TaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class ProjectTaskViewset(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    slug_field = 'project'
    slug_url_kwarg = 'project_id'

    def initialize_request(self, request, *args, **kwargs):
        request = super().initialize_request(request, *args, **kwargs)
        request.data[self.slug_field] = self.kwargs[self.slug_url_kwarg]
        return request

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(project=self.kwargs[self.slug_url_kwarg])
        return queryset.order_by('order')
