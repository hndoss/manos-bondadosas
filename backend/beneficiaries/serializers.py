from rest_framework import serializers
from .models import Beneficiary


class BeneficiarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Beneficiary
        fields = ('id', 'first_name', 'last_name', 'age', 'sex', 'email', )