"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from rest_framework_swagger.views import get_swagger_view

admin.autodiscover()
schema_view = get_swagger_view(title='API')

urlpatterns = [
    url('doc/', schema_view),
    url('api/v1/people/', include('people.urls')),
    url('api/v1/projects/', include('projects.urls'))
]

urlpatterns += i18n_patterns(
    url('admin/', admin.site.urls)
)

admin.site.site_header = "Manos Bondadosas"
admin.site.site_title = "Manos Bondadosas Admin"
admin.site.index_title = "Welcome to Manos Bondadosas"