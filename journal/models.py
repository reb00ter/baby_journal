from django.utils.translation import ugettext as _
from django.db import models


# Create your models here.
class Entry(models.Model):
    datetime = models.DateTimeField(verbose_name=_("time and date"),
                                    auto_now_add=True)
    title = models.CharField(verbose_name=_("title"), max_length=100)
    text = models.TextField(verbose_name=_("description"))