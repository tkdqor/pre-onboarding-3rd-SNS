from rest_framework import serializers

from posts.models import Post


class PostsCreateSerializer(serializers.ModelSerializer):
    """
    Assignee : 상백

    게시글을 생성하는 시리얼라이저입니다.
    context 딕셔너리로 token 인증된 작성자 객체를 확인합니다.
    제목, 내용, 해시태그 정보를 필수로 입력하게끔 설정합니다.
    """

    def create(self, validated_data):
        writer = self.context["writer"]
        post = Post(writer=writer, **validated_data)
        post.save()
        return post

    class Meta:
        model = Post
        fields = ("title", "writer", "content", "created_at", "updated_at", "is_deleted", "hashtags", "views")
        read_only_fields = ["writer", "created_at", "updated_at", "is_deleted", "views"]
