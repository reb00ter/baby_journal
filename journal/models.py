from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext as _
from django.db import models
from core.models import User


# Create your models here.
PARENT_ROLE_CHOICES = (
    ('M', _("Mother")),
    ('F', _("Father"))
)


class BabiesParent(models.Model):
    user = models.ForeignKey(User, verbose_name=_("user"))
    baby = models.ForeignKey("Baby", verbose_name=_("baby"))
    role = models.CharField(max_length=1, choices=PARENT_ROLE_CHOICES, default='M', verbose_name=_("role"))

    class Meta:
        unique_together = ['user', 'baby', 'role']
        verbose_name = _("parents relation")
        verbose_name_plural = _("parents relations")


class Baby(models.Model):
    parents = models.ManyToManyField(User, verbose_name=_("parent"))
    name = models.CharField(max_length=100, verbose_name=_("name"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("baby")
        verbose_name_plural = _("babies")


class EntriesManager(models.Manager):
    def get_queryset(self):
        return super(EntriesManager, self).get_queryset().prefetch_related('baby')


class Entry(models.Model):
    baby = models.ForeignKey(Baby, verbose_name=_("baby"))
    datetime = models.DateTimeField(verbose_name=_("time and date"),
                                    auto_now_add=True)
    title = models.CharField(verbose_name=_("title"), max_length=100)
    text = models.TextField(verbose_name=_("description"))
    weight = models.DecimalField(verbose_name=_("weight"), max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(verbose_name=_("height"), max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return "%s, %s - %s" % (self.datetime, self.title, self.baby__name)

    class Meta:
        verbose_name = _("entry")
        verbose_name_plural = _("entries")
        default_manager_name = EntriesManager
