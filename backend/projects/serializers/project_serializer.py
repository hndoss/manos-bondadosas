from rest_framework import serializers
from ..models import Project
from people.serializers.collaborator_serializer import CollaboratorSerializer
from people.serializers.beneficiary_serializer import BeneficiarySerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description',
                  'direction', 'status', 'category', 'beneficiaries', 'collaborators')


class ProjectDetailSerializer(serializers.ModelSerializer):
    collaborators = CollaboratorSerializer(many=True, read_only=True)
    beneficiaries = BeneficiarySerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'direction', 'status',
                  'category', 'beneficiaries', 'collaborators', )
