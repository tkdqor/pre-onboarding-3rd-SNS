from django.urls import path

from accounts.views import SignUpView

app_name = "accounts"

urlpatterns = [
    path("v1/users/signup", SignUpView.as_view()),
]
