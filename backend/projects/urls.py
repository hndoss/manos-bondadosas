from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('categories', views.CategoryViewset)
router.register('statuses', views.StatusViewset)
router.register('tasks', views.TaskViewset)
router.register(r'(?P<project_id>\d+)/tasks',
                views.ProjectTaskViewset, basename='project_tasks')
router.register('', views.ProjectViewset)


urlpatterns = [
    path('', include(router.urls)),
]
