from django.urls import path

from accounts.views import SignInView, SignUpView

app_name = "accounts"

urlpatterns = [
    path("v1/users/signup", SignUpView.as_view()),
    path("v1/users/signin", SignInView.as_view()),
]
