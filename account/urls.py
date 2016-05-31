from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.acclogreg, name='account'),
    url(r'^authview$', views.authview, name='authview'),
    url(r'^register$', views.register, name='register'),
    url(r'^update_password$', views.update_password, name='update_password'),
    url(r'^update_user_info$', views.update_user_info, name='update_user_info'),
    url(r'^fetch_user_data$', views.fetch_user_data, name='fetch_user_data'),
    url(r'^management$', views.accmanage, name='management'),
]
