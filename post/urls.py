from django.conf.urls import url, include
from . import views

app_name = 'post'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^gallery/(?P<post_id>[0-9]+)$', views.detail, name="detail"),
    url(r'^gallery/(?P<post_id>[0-9]+)/$', views.detail, name='gallery'),
    url(r'^upload_image$', views.upload_post, name='upload_post'),
    url(r'^post_comment', views.post_comment, name="post_comment"),
    url(r'^like_post/(?P<post_id>[0-9]+)', views.user_post_like, name="like_post"),
    url(r'^dislike_post/(?P<post_id>[0-9]+)', views.user_post_dislike, name="dislike_post"),
    url(r'^favorite_post/(?P<post_id>[0-9]+)', views.user_post_favorite, name="favorite_post"),

    url(r'^like_comment/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.user_comment_like, name="like_comment"),
    url(r'^dislike_comment/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.user_comment_dislike, name="dislike_comment"),
    url(r'^favorite_comment/(?P<post_id>[0-9]+)/(?P<comment_id>[0-9]+)', views.user_comment_favorite, name="favorite_comment"),


    url(r'^next_post/(?P<post_id>[0-9]+)', views.post_next, name="next_post"),
    url(r'^prev_post/(?P<post_id>[0-9]+)', views.post_prev, name="prev_post"),



]
