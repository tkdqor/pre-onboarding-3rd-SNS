from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from config.permissions import IsOwner
from posts.serializers import PostsCreateSerializer, PostsRecordSerializer

from .models import Post

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

    permission_classes = [IsOwner]
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


# url : GET,PUT,PATCH api/v1/posts/<post_id>
class PostView(APIView):
    """
    Assignee : 상백

    GET : 게시글 상세보기를 수행하는 메서드입니다.
    PUT : 게시글을 수정하는 메서드입니다.
    PATCH : 게시글을 삭제 및 복구하는 메서드입니다.
    """

    permission_classes = [IsOwner]
    serializer = PostsRecordSerializer

    """JWT 인증방식 클래스 지정하기"""
    authentication_classes = [JWTAuthentication]

    def get_object_and_check_permission(self, obj_id):
        """
        Assignee : 상백

        obj_id : int

        input 인자로 Post 객체를 가져와 퍼미션 검사를 하는 메서드입니다.
        DoesNotExist 에러 발생 시 None을 리턴합니다.
        APIView 클래스에 정의된 check_object_permissions 메서드를 override해서 검사를 진행합니다.
        """

        try:
            object = Post.objects.get(id=obj_id)
        except Post.DoesNotExist:
            return

        self.check_object_permissions(self.request, object)
        return object

    def get(self, request, post_id):
        """
        Assignee : 상백

        post_id : int

        게시글 상세보기를 위한 메서드입니다.
        횟수 제한 없이 조회수가 증가합니다.
        """

        post = self.get_object_and_check_permission(post_id)

        """횟수 제한 없이 조회수 증가"""
        if request:
            post.views += 1
            post.save()

        if not post:
            return Response({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(PostsRecordSerializer(post).data, status=status.HTTP_200_OK)

    def put(self, request, post_id):
        """
        Assignee : 상백

        post_id : int

        게시글 수정을 위한 메서드입니다. partial 옵션을 사용해 일부분만 수정이 가능합니다.
        title, content, hashtags 필드만 수정이 가능합니다.
        """

        post = self.get_object_and_check_permission(post_id)

        if not post:
            return Response({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            if request.data["is_deleted"] is not None:
                return Response({"error": "잘못된 요청입니다."}, status=status.HTTP_400_BAD_REQUEST)

        except KeyError:
            pass

        serializer = PostsRecordSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "게시글 수정 성공"}, status=status.HTTP_200_OK)

    def patch(self, request, post_id):
        """
        Assignee : 상백

        post_id : int

        게시글 기록 객체를 삭제 및 복구하기 위한 메서드입니다.
        is_deleted 필드의 값을 True 또는 False로 변경할 수 있습니다.
        """

        post = self.get_object_and_check_permission(post_id)
        if not post:
            return Response({"error": "해당 게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)

        try:
            if request.data["is_deleted"] == True:
                post.is_deleted = True
                post.save()
                return Response({"message": "게시글 삭제 성공"}, status=status.HTTP_200_OK)
            elif request.data["is_deleted"] == False:
                post.is_deleted = False
                post.save()
                return Response({"message": "게시글 복구 성공"}, status=status.HTTP_200_OK)
        except KeyError:
            return Response({"message": "게시글 삭제 및 복구 실패. is_deleted를 수정해주세요"}, status=status.HTTP_400_BAD_REQUEST)
