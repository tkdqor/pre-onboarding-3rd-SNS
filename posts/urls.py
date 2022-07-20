from django.urls import path

from posts.views import PostsView

app_name = "posts"

urlpatterns = [
    path("api/v1/posts", PostsView.as_view()),
]
