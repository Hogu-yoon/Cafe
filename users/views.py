from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from users.models import Profile
from users.permissions import CustomReadOnly
from users.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import status


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class ProfileView(generics.RetrieveUpdateAPIView):
    # 필요한 퍼미션은 해당 apiView서 생성한다
    permission_classes = [CustomReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
