from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from parts_manager.website import views as app_views
from parts_manager.parts.viewsets import PartViewSet
from parts_manager.products.viewsets import ProductViewSet, RetailerViewSet
from parts_manager.purchases.viewsets import PurchaseViewSet
from parts_manager.robots.viewsets import RobotViewSet, RobotPartViewSet


router = routers.DefaultRouter()

router.register('parts', PartViewSet)
router.register('products', ProductViewSet)
router.register('purchases', PurchaseViewSet)
router.register('retailers', RetailerViewSet)
router.register('robots', RobotViewSet)
router.register('robotparts', RobotPartViewSet)

app_name = 'website'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^admin/doc/',
        include('django.contrib.admindocs.urls')
    ),

    url(
        r'accounts/',
        include('django.contrib.auth.urls')
    ),

    url(
        r'^$',
        app_views.MainView.as_view(),
        name='main'
    ),

    url(
        r'^api/',
        include((router.urls, 'app_name'), namespace='api')
    ),
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(
        r'^parts/',
        include('parts_manager.parts.urls', namespace='part'),
        name='part_root',
    ),

    url(
        r'^projects/',
        include('parts_manager.projects.urls', namespace='project'),
        name='project_root',
    ),

]
