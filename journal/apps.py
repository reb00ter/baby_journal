from django.apps import AppConfig
from django.utils.translation import ugettext as _


class JournalConfig(AppConfig):
    name = 'journal'
    verbose_name = _('journal')