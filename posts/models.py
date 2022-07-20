from django.db import models

from accounts.models import User

"""Create your models here."""


class Post(models.Model):
    """
    Assignee : 상백

    SNS 서비스 게시글에 대한 정보를 나타내는 모델입니다.
    """

    title = models.CharField("제목", max_length=30)
    writer = models.ForeignKey(to=User, verbose_name="작성자", on_delete=models.CASCADE, related_name="user_post")
    content = models.TextField("내용")
    created_at = models.DateTimeField("작성일자", auto_now_add=True)
    updated_at = models.DateTimeField("수정일자", auto_now=True)
    is_deleted = models.BooleanField("삭제여부", default=False)


class Tag(models.Model):
    """
    Assignee : 상백

    SNS 서비스 게시글의 해시태그 종류를 나타내는 모델입니다.
    생성된 해시태그 목록을 보여줍니다.
    """

    name = models.CharField("해시태그", max_length=50)


class PostTag(models.Model):
    """
    Assignee : 상백

    SNS 서비스 게시글이 현재 어떤 해시태그에 속해있는지 보여주는 모델입니다.
    Post 모델과 1:N 그리고 Tag 모델과 1:N 관계를 형성합니다.
    """

    post = models.ForeignKey(to=Post, verbose_name="게시글", on_delete=models.CASCADE, related_name="post_tag")
    tag = models.ForeignKey(to=Tag, verbose_name="해시태그", on_delete=models.CASCADE, related_name="tag_post")
