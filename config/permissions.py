from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Assignee : 상백

    has_permission : 로그인 한 유저는 모두 접근 가능

    has_object_permission(오브젝트 접근 권한)
    - 조회 요청(GET, HEAD, OPTIONS)에 대해서는 로그인된 유저에 한해 접근 가능
    - 그 외에는 작성자가 본인일 경우 접근 가능
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return obj.writer.id == request.user.id
