from django.conf import settings

TAGS_SCAN_MODULES = getattr(
    settings,
    'CONTENT_BBCODE_SCAN_MODULES',
    dict([(app_name.split('.')[-1], app_name + ".tags")
          for app_name in settings.INSTALLED_APPS])
)
