from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

"""Create your models here."""


class CustomUserManager(BaseUserManager):
    """
    Assignee : 상백

    custom user model 사용을 위한 UserManager 클래스 및
    create_user, create_superuser 함수를 정의합니다.
    """

    def create_user(self, email, password):
        if not email:
            raise ValueError("이메일을 ID로 사용합니다. 이메일을 입력해주세요.")
        user = self.model(
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """python manage.py createsuperuser 사용 시 해당 함수가 사용됨"""
        user = self.create_user(
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    """
    Assignee : 상백

    이메일을 ID로 사용하는 유저 모델입니다.
    """

    email = models.EmailField("이메일 주소", max_length=100, unique=True)
    password = models.CharField("비밀번호", max_length=128)

    """is_active가 False일 경우 계정이 비활성화됨"""
    is_active = models.BooleanField("활성화", default=True)

    """is_staff에서 해당 값 사용"""
    is_admin = models.BooleanField("관리자", default=False)

    created_at = models.DateTimeField("생성일", auto_now_add=True)
    updated_at = models.DateTimeField("수정일", auto_now=True)

    """"
    # id로 사용할 필드 지정.
    # 로그인 시 USERNAME_FIELD에 설정된 필드와 password가 사용됩니다.
    """
    USERNAME_FIELD = "email"

    """user를 생성할 때 입력받을 필드 지정"""
    REQUIRED_FIELDS = []

    """custom user 생성 시 필요"""
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        로그인 사용자의 특정 테이블의 crud 권한을 설정, perm table의 crud 권한을 설정합니다.
        admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False입니다.
        """
        return True

    def has_module_perms(self, app_label):
        """
        로그인 사용자의 특정 app에 접근 가능 여부를 설정, app_label에는 app 이름이 들어갑니다.
        admin일 경우 항상 True, 비활성 사용자(is_active=False)의 경우 항상 False입니다.
        """
        return True

    @property
    def is_staff(self):
        """admin 권한 설정"""
        return self.is_admin
