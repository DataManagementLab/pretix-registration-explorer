from django.utils.translation import gettext_lazy

try:
    from pretix.base.plugins import PluginConfig
except ImportError:
    raise RuntimeError("Please use pretix 2.7 or above to run this plugin!")

__version__ = '1.0.0'


class PluginApp(PluginConfig):
    name = 'pretix_registration_explorer'
    verbose_name = 'Registration Explorer'

    class PretixPluginMeta:
        name = gettext_lazy('Registration Explorer')
        author = 'Benjamin Hättasch'
        description = gettext_lazy('Allow to explore and filter registrations on a public page')
        visible = True
        version = __version__
        category = 'FEATURE'
        compatibility = "pretix>=3.7.0"

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_registration_explorer.PluginApp'
