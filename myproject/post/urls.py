from django.urls import path
from rest_framework import routers
from .views import PostViewSet

router = routers.SimpleRouter()
router.register('posts', PostViewSet)

urlpatternw = router.urls