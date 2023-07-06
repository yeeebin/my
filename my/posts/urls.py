from django.urls import path
from rest_framework import routers

from .views import PostViewSet

router = routers.SimpleRouter() #router을 통해 URL 일일이 지정하지 않아도 일정한 규칙의 URL 만들기 가능
router.register('posts', PostViewSet) #ViewSet : mixin을 기반으로 작성한 코드 

urlpatterns = router.urls #router가 간단히 해쥼