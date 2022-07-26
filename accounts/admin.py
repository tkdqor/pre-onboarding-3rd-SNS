from django.contrib import admin

from .models import User


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    """
    Assignee : 상백

    User 모델을 어드민 사이트에 설정합니다.
    """

    list_display = ("id", "email", "password", "is_active", "is_admin", "created_at", "updated_at")
