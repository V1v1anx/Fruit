from django.conf.urls import url
from .views import *
urlpatterns = [
  url(r'^$',index_views,name='index'),
  url(r'^login/$',login_views,name='login'),
  url(r'^register/$',register_views,name='reg'),
]