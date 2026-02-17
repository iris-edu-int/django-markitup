from __future__ import unicode_literals
from urllib.parse import urljoin
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage


def absolute_url(path):
    if (
        path.startswith("http://")
        or path.startswith("https://")
        or path.startswith("/")
    ):
        return path
    try:
        return staticfiles_storage.url(path)
    except ValueError:
        return urljoin(settings.STATIC_URL, path)
