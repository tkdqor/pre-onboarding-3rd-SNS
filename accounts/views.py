from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.serializers import SignUpSerializer

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
