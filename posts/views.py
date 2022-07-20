from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from posts.serializers import PostsCreateSerializer

"""Create your views here."""


# url : POST api/v1/posts
class PostsView(APIView):
    """
    Assignee : 상백

    게시글을 생성하는 APIView입니다.
    제목, 내용, 해시태그 정보를 필수로 입력합니다.
    {
        "title" : "여름날",
        "content" : "유난히 맑은 하늘 아래",
        "hashtags" : "#소설,#문학"
    }
    context 딕셔너리로 token 인증된 작성자 객체를 보내주어 클라이언트가 작성자 id를 입력하지 않게 설정했습니다.
    """

    permission_classes = [IsAuthenticated]
    serializer = PostsCreateSerializer

    """JWT 인증방식 클래스 지정하기"""
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        context = {"writer": request.user}

        serializer = self.serializer(data=request.data, context=context)
        if serializer.is_valid():
            serializer.save()
            res = Response(
                {
                    "message": "게시글이 생성되었습니다.",
                },
                status=status.HTTP_201_CREATED,
            )
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
