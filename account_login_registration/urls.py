from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.acclogreg, name='account_login_registration'),
]