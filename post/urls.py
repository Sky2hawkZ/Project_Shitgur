from django.conf.urls import url #, include

from . import views
from django.views.generic import TemplateView

app_name = 'post'

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='post/frontpage.html'), name='home'),

    #
    url(r'^$', views.index, name='index'),

    #/gallery/1/
    url(r'^gallery/(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
]
