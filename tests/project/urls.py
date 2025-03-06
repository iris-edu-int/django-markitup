from django.urls import path, include
from django.views.generic.base import TemplateView

from .forms import DemoForm


urlpatterns = [
    path(
        '',
        TemplateView.as_view(template_name='demo.html'),
        {'form': DemoForm()},
        name='demo',
        ),
    path('markitup/', include('markitup.urls')),
]
