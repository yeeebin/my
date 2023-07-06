from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) #nested serializer-serializer 안에 또 다른 serilalizer를 넣어 이중으로 연결되는 구조

    class Meta:
        model = Post
        fields = ("pk", "profile","body", "title", "images", "published_date", "likes")


class PostCreateSerializer(serializers.ModelSerializer):   # 유저가 입력하는 정보
    class Meta:
        model = Post
        fields = ("title", "category", "body", "images")