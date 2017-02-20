from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _


# Create your models here.
class User(AbstractUser):
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


