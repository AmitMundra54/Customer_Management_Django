from django.conf.urls import url, include
from rest_framework import routers
from core.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'^users',UserViewSet)

urlpatterns = [
               url(r'', include(router.urls)),
               url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))

    ]
#