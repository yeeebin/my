from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSelializer, ProfileSerializer
from .models import Profile


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer



class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer



class LoginView(generics.GenericAPIView):
    serializer_class = LoginSelializer

    def post(self, request):
        serialzer = self.get_serializer(data=request.data)
        serialzer.is_valid(raise_exception=True)
        token = serialzer.validated_data
        return Response({"token":token.key}, status=status.HTTP_200_OK)


# Create your views here.
