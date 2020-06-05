from rest_framework import serializers
from ..models import Project, ProjectBeneficiary
from people.serializers.collaborator_serializer import CollaboratorSerializer
from people.serializers.beneficiary_serializer import BeneficiarySerializer


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'description',
                  'direction', 'status', 'category',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    collaborators = CollaboratorSerializer(many=True)
    beneficiaries = BeneficiarySerializer(many=True)

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'direction', 'status',
                  'category', 'beneficiaries', 'collaborators', )


class ProjectBeneficiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectBeneficiary
        fields = ('project_id', 'beneficiary_id', )
