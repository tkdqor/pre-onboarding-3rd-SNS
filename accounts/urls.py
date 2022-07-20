from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from accounts.views import SignInView, SignUpView

app_name = "accounts"

urlpatterns = [
    path("v1/users/signup", SignUpView.as_view()),
    path("v1/users/signin", SignInView.as_view()),
    path("v1/token/refresh", TokenRefreshView.as_view()),
]
