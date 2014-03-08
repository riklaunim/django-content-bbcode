from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    '',

    url(r'^$', 'content_bbcode_demo.demo_application.views.test_view'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
