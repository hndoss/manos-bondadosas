from rest_framework import viewsets, permissions
from ..serializers import StatusSerializer
from ..models import Status


class StatusViewset(viewsets.ModelViewSet):
    serializer_class = StatusSerializer
    queryset = Status.objects.all()
