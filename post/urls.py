from django.conf.urls import url, include
from django.views.generic import TemplateView
from . import views

app_name = 'post'

urlpatterns = [
# url(r'^$', TemplateView.as_view(template_name='post/frontpage.html'), name='home'),

#
url(r'^$', views.index, name='index'),

#/gallery/1/
url(r'^gallery/(?P<post_id>[0-9]+)/$', views.detail, name='gallery'),
url(r'^upload_image$', views.upload_post, name='upload_post'),
]
