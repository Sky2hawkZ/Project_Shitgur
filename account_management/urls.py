from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.accmanage, name='account_management'),
]