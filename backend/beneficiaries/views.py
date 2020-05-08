
from rest_framework import viewsets, permissions
from .serializers import BeneficiarySerializer
from .models import Beneficiary


class BeneficiaryView(viewsets.ModelViewSet):
    serializer_class = BeneficiarySerializer
    queryset = Beneficiary.objects.all()