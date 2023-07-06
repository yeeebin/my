from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets

from users.models import Profile
from .models import Post
from .permissions import CustomReadOnly
from .serializers import PostSerializer, PostCreateSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [CustomReadOnly]  #permission_classes 속성은 리스트 형태로 여러 개의 권한 클래스를 입력받는다. 
#따라서 CustomReadOnly를 리스트 형태로 입력한 것은 해당 API 뷰에 CustomReadOnly 권한 클래스를 적용하고, GET, HEAD, OPTIONS 메서드에 대해서만 요청을 허용하기 위해서
    filter_backends = [DjangoFilterBackend]
    filterset_filds = ['author', 'likes']
    
    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return PostSerializer
        return PostCreateSerializer
    
    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(author=self.request.user, profile=profile)




# Create your views here.
