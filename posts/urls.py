from django.urls import path

from posts.views import PostLikeView, PostsView, PostView

app_name = "posts"

urlpatterns = [
    path("api/v1/posts", PostsView.as_view()),
    path("api/v1/posts/<post_id>", PostView.as_view()),
    path("api/v1/posts/<post_id>/likes", PostLikeView.as_view()),
]
