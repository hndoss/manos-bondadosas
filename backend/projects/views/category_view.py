from rest_framework import viewsets, permissions
from ..serializers import CategorySerializer
from ..models import Category


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
