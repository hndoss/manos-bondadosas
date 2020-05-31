from rest_framework import serializers
from ..models import Project
from collaborators.serializers.collaborator_serializer import CollaboratorSerializer
from beneficiaries.serializers import BeneficiarySerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'direction', 'status', 'category',)
