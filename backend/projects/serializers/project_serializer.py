from rest_framework import serializers
from ..models import Project
from collaborators.serializers.collaborator_serializer import CollaboratorSerializer


class ProjectSerializer(serializers.ModelSerializer):
    collaborators = CollaboratorSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'direction',
                  'collaborators', 'status', 'category',)
