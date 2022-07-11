from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response

from users.models import Profile
from users.permissions import CustomReadOnly
from users.serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import status

from django.contrib import auth

'''
회원 생성 뷰 (post 처리기능) 
'''
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


'''
회원 로그인 뷰 (generic API 뷰를 사용해서 로그인 부분 처리)
회원이 맞다면 해당 토큰으로 반환
'''
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key,"UserID":token.user_id}, status=status.HTTP_200_OK)

'''
회원 상세 페이지 단건 조회 및 수정 기능(GET 과 PUT,PATH 처리)

'''
class ProfileView(generics.RetrieveUpdateAPIView):
    # 필요한 퍼미션은 해당 apiView서 생성한다
    permission_classes = [CustomReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


