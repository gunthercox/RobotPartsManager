from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
#from rest_framework import routers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/',
        include('django.contrib.admindocs.urls')
    ),

    url(r'^login/$',
        auth_views.login,
        {'template_name': 'login.html'}
    ),
    url(r'^logout/$', auth_views.logout),
    url(r'^api-auth/',
        include('rest_framework.urls',
        namespace='rest_framework')
    ),

    url(r'',
        include('social.apps.django_app.urls',
        namespace='social')
    ),

    url(r'^api/oauth/',
        include(
            'oauth2_provider.urls',
            namespace='oauth2_provider'
        ),
    ),

    url(r'^api/',
        include(
            'parts_manager.core.api.urls',
            namespace='api'
        ),
        name='api_root',
    ),
]
