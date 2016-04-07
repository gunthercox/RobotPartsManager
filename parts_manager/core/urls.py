from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from rest_framework import routers
from parts_manager.robots.api import RobotViewSet
from parts_manager.parts.api import PartViewSet
from parts_manager.products.api import ProductViewSet, RetailerViewSet


router = routers.DefaultRouter()

router.register('parts', PartViewSet)
router.register('products', ProductViewSet)
router.register('retailers', RetailerViewSet)
router.register('robots', RobotViewSet)


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

    url(r'',
        include('social.apps.django_app.urls',
        namespace='social')
    ),

    url(r'^api/',
        include(router.urls,
        namespace='api'),
        name='api_root',
    ),
    url(r'^api-auth/',
        include('rest_framework.urls',
        namespace='rest_framework')
    ),

    url(r'^api/oauth/',
        include(
            'oauth2_provider.urls',
            namespace='oauth2_provider'
        ),
    ),
]
