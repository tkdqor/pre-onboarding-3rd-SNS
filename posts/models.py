from django.db import models

from accounts.models import User


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
    hashtags = models.TextField("해시태그")
    views = models.PositiveIntegerField("조회수", default=0)
    likes = models.ManyToManyField(to=User, blank=True, related_name="user_like")
