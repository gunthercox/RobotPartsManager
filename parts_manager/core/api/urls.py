from rest_framework import routers
from parts_manager.robots.api import RobotViewSet
from parts_manager.parts.api import PartViewSet


router = routers.DefaultRouter()

router.register(
    'robots',
    RobotViewSet,
    base_name='robots'
)

router.register(
    'parts',
    PartViewSet,
    base_name='parts'
)

urlpatterns = router.urls
