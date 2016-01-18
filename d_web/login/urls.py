from django.conf.urls import url

from . import views


app_name = 'login'

urlpatterns = [
    # index page
    url(r'^$', views.IndexView.as_view(), name='index'),
    # after login user will be redirected to this url
    url(r'^logged_in/$', views.logged_in, name='logged_in'),
    # using default django auth views with custom templates
    url(r'^logout/$', views.logged_in, name='logout'),
]