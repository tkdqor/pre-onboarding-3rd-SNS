from rest_framework import serializers

from posts.models import Post


class PostsSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    게시글 생성 및 목록 조회 관련 시리얼라이저입니다.
    게시글 생성 시, context 딕셔너리로 token 인증된 작성자 객체를 확인합니다.
    제목, 내용, 해시태그 정보를 필수로 입력하게끔 설정합니다.

    게시글 목록 조회의 경우, 제목, 작성자, 해시태그, 작성일, 좋아요 수, 조회수가 포함됩니다.
    """

    writer = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    def get_writer(self, obj):
        writer = obj.writer.email
        return writer

    def get_likes(self, obj):
        likes_count = obj.likes.count()
        return likes_count

    def create(self, validated_data):
        writer = self.context["writer"]
        post = Post(writer=writer, **validated_data)
        post.save()
        return post

    class Meta:
        model = Post
        fields = ("id", "title", "writer", "content", "hashtags", "likes", "views", "created_at")
        read_only_fields = ["writer", "created_at", "likes", "views"]


class PostsRecordSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    게시글 상세보기, 수정, 삭제 및 복구 관련 시리얼라이저입니다.
    """

    writer = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    def get_writer(self, obj):
        writer = obj.writer.email
        return writer

    def get_likes(self, obj):
        likes_count = obj.likes.count()
        return likes_count

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "writer",
            "content",
            "hashtags",
            "likes",
            "views",
            "created_at",
            "updated_at",
            "is_deleted",
        )
        read_only_fields = ["id", "writer", "likes", "views", "created_at", "updated_at", "is_deleted"]
