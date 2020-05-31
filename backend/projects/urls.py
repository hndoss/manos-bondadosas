from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewset)
router.register('statuses', views.StatusViewset)
router.register('tasks', views.TaskViewset)
router.register(r'(?P<project_id>\d+)/tasks',
                views.ProjectTaskViewset, basename='project_tasks')
router.register(r'(?P<project_id>\d+)/beneficiaries',
                views.ProjectBeneficiaryViewset, basename='beneficiaries')
router.register(r'(?P<project_id>\d+)/collaborators',
                views.ProjectCollaboratorViewset, basename='collaborators')
router.register('', views.ProjectViewset)


urlpatterns = [
    path('', include(router.urls)),
]
