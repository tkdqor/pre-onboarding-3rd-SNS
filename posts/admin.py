from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    """
    Assignee : 상백

    Post 모델을 어드민 사이트에 설정합니다.
    """

    list_display = ("id", "title", "writer", "content", "created_at", "updated_at", "is_deleted", "hashtags", "views")
