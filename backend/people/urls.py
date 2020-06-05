from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('beneficiaries', views.BeneficiaryView)
router.register('collaborators', views.CollaboratorView)

urlpatterns = [
    path('', include(router.urls)),
]