from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.serializers import (
    SignInSerializer,
    SignUpSerializer,
    UserLikesSerializer,
    UserTokenObtainPairSerializer,
    UserTrashSerializer,
)
from config.permissions import IsOwner

"""Create your views here."""


# url : POST api/v1/users/signup
class SignUpView(APIView):
    """
    Assignee : 상백

    회원가입을 진행하는 APIView입니다.
    권한은 누구나 접근할 수 있게 설정하고 회원가입 성공 시, 201 code를 응답합니다.
    """

    permission_classes = [AllowAny]
    serializer = SignUpSerializer

    def post(self, request):
        serializer = self.serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            res = Response(
                {
                    "message": "회원가입에 성공했습니다.",
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# url : POST api/v1/users/signin
class SignInView(APIView):
    """
    Assignee : 상백

    로그인을 진행하는 APIView입니다.
    로그인 성공 시, 클라이언트에게 access token과 refresh token을 리턴합니다.
    """

    permission_classes = [AllowAny]
    serializer = SignInSerializer

    def post(self, request):
        user = authenticate(
            request,
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        if not user:
            return Response({"error": "이메일 또는 비밀번호를 잘못 입력했습니다."}, status=status.HTTP_404_NOT_FOUND)

        login(request, user)

        token = UserTokenObtainPairSerializer.get_token(user)

        res = Response(
            {
                "message": f"{user.email}님 반갑습니다!",
                "token": {
                    "access": str(token.access_token),
                    "refresh": str(token),
                },
            },
            status=status.HTTP_200_OK,
        )
        return res


# url : GET api/v1/users/likes
class UserLikesView(APIView):
    """
    Assignee : 상백

    GET : 로그인된 유저의 게시글 좋아요 목록을 응답하는 메서드입니다.
    """

    permission_classes = [IsOwner]
    serializer = UserLikesSerializer

    """JWT 인증방식 클래스 지정하기"""
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Assignee : 상백

        유저의 게시글 좋아요 목록을 조회합니다.
        목록에는 게시글의 id와 제목이 포함됩니다.
        """

        likes = request.user.user_like.filter(is_deleted=False)
        serializer = self.serializer(likes, many=True)

        if not likes:
            return Response({"error": "좋아요를 누른 게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)


# url : GET api/v1/users/trash
class UserTrashView(APIView):
    """
    Assignee : 상백

    GET : 로그인된 유저의 게시글 삭제 목록을 응답하는 메서드입니다.
    """

    permission_classes = [IsOwner]
    serializer = UserTrashSerializer

    def get(self, request):
        """
        Assignee : 상백

        유저의 게시글 삭제 목록을 조회합니다.
        목록에는 게시글의 id와 제목, 삭제여부가 포함됩니다.
        """

        trash = request.user.user_post.filter(is_deleted=True)
        serializer = self.serializer(trash, many=True)

        if not trash:
            return Response({"error": "삭제된 게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)
