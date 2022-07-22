from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from config.permissions import IsOwner
from posts.serializers import PostsRecordSerializer, PostsSerializer

from .models import Post

"""Create your views here."""


# url : GET, POST api/v1/posts
class PostsView(APIView):
    """
    Assignee : 상백

    GET : 게시글 목록을 조회하는 메서드입니다.
    POST : 게시글을 생성하는 메서드입니다.
    """

    permission_classes = [IsOwner]
    serializer = PostsSerializer

    """JWT 인증방식 클래스 지정하기"""
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        """
        Assignee : 상백

        게시글 목록을 조회합니다.
        목록에는 제목, 작성자, 해시태그, 작성일, 조회수가 포함됩니다.

        쿼리 파라미터를 통해 입력한 키워드가 제목에 포함된 게시글 목록을 응답합니다.
        """

        posts = Post.objects.filter(is_deleted=False)
        serializer = self.serializer(posts, many=True)

        """키워드 검색 기능"""
        search_keyword = request.GET.get("search")
        if search_keyword:
            posts = Post.objects.filter(Q(title__icontains=search_keyword))
            serializer = self.serializer(posts, many=True)

        if not posts:
            return Response({"error": "게시글이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Assignee : 상백

        제목, 내용, 해시태그 정보를 필수로 입력합니다.
        {
        "title" : "여름날",
        "content" : "유난히 맑은 하늘 아래",
        "hashtags" : "#소설,#문학"
        }
        context 딕셔너리로 token 인증된 작성자 객체를 보내주어 클라이언트가 작성자 id를 입력하지 않게 설정했습니다.
        """

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


# url : POST api/v1/posts/<post_id>/likes
class PostLikeView(APIView):
    """
    Assignee : 상백

    POST : 특정 게시글에 좋아요 및 좋아요 취소를 설정하는 메서드입니다.
    """

    permission_classes = [IsAuthenticated]
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

    def post(self, request, post_id):
        """
        Assignee : 상백

        post_id를 입력하고 요청했을 때, Post와 User의 M:N관계 모델에 데이터 생성
        만약 이미 있다면 데이터 삭제
        """

        post = self.get_object_and_check_permission(post_id)
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            return Response({"message": f"{post_id}번 게시글 좋아요 취소 성공"}, status=status.HTTP_200_OK)
        else:
            post.likes.add(request.user)
            return Response({"message": f"{post_id}번 게시글 좋아요 성공"}, status=status.HTTP_200_OK)
