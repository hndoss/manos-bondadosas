from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('categories', views.ProjectCategoryView)
router.register('statuses', views.ProjectStatusView)
router.register('', views.ProjectView)


urlpatterns = [
    path('', include(router.urls)),
]
