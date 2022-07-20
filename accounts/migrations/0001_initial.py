# Generated by Django 4.0.6 on 2022-07-20 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='이메일 주소')),
                ('password', models.CharField(max_length=128, verbose_name='비밀번호')),
                ('is_active', models.BooleanField(default=True, verbose_name='활성화')),
                ('is_admin', models.BooleanField(default=False, verbose_name='관리자')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='생성일')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
