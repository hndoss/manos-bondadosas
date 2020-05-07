
from rest_framework import viewsets, permissions
from ..serializers import CollaboratorSerializer
from ..models import Collaborator


class CollaboratorView(viewsets.ModelViewSet):
    serializer_class = CollaboratorSerializer
    queryset = Collaborator.objects.all()