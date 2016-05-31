from django.conf.urls import url, include

from django.views.generic import TemplateView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='post/index.html'), name='home'),
    url(r'^gallery/(?P<post_id>[0-9]+)$', views.detail, name="detail"),
    url(r'^post_comment', views.post_comment, name="post_comment"),
    url(r'^like_post', views.user_post_like, name="like_post"),
    url(r'^dislike_post', views.user_post_dislike, name="dislike_post"),
    url(r'^favorite_post', views.user_post_favorite, name="favorite_post"),



]
