from django.conf.urls import url, include

from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='post/frontpage.html'), name='home'),
    url(r'^gallery/(?P<post_id>[0-9]+)$', views.detail, name="detail"),
]
