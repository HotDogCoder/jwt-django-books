from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager

from django.db import models
from django.conf import settings
import os

# Create your models here.
def user_profile_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    profile_pic_name = 'user/{0}/profile.jpg'.format(instance.account)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

def user_banner_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    banner_pic_name = 'user/{0}/banner.jpg'.format(instance.account)
    full_path = os.path.join(settings.MEDIA_ROOT, banner_pic_name)

    if os.path.exists(full_path):
        os.remove(full_path)

class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)  # Use AutoField for integer primary key
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    last_login = models.DateTimeField(_('last login'), blank=True, null=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)

    verified = models.BooleanField(default=False)
    requested_verified = models.BooleanField(default=False)

    picture = models.ImageField(
        default='user/user_default_profile.png',
        upload_to=user_profile_directory_path,
        blank=True, null=True, verbose_name='Picture'
    )
    banner = models.ImageField(
        default='user/user_default_bg.jpg',
        upload_to=user_banner_directory_path,
        blank=True, null=True, verbose_name='Banner'
    )

    location = models.CharField(max_length=50, null=True, blank=True)
    url = models.CharField(max_length=80, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    profile_info = models.TextField(max_length=150, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name']

    objects = CustomUserManager()

    class Meta:
        db_table = "user_account"

    def __str__(self):
        return self.email