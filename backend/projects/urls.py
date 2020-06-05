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
                views.ProjectBeneficiaryViewset, basename='project_beneficiaries')
router.register(r'(?P<project_id>\d+)/collaborators',
                views.ProjectCollaboratorViewset, basename='project_collaborators')
router.register(r'(?P<project_id>\d+)',
                views.ProjectDetailViewset, basename='project_details')
router.register('', views.ProjectViewset)


urlpatterns = [
    path('', include(router.urls)),
]
