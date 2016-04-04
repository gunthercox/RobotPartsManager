from rest_framework import routers
from parts_manager.robots.api import RobotViewSet


router = routers.DefaultRouter()

router.register(
    'robots',
    RobotViewSet,
    base_name='robots'
)

urlpatterns = router.urls
