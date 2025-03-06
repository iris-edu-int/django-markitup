from __future__ import unicode_literals

from django.urls import path, include

urlpatterns = [
    path('markitup/', include('markitup.urls')),
]
