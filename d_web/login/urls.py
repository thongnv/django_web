from django.conf.urls import url

from . import views

app_name = 'login'

urlpatterns = [
    # index page
    url(r'^$', views.LoginView.as_view(), name='login'),
    url(r'^index/$', views.IndexView.as_view(), name='index'),
    url(r'^logout/$', views.logged_in, name='logout'),
]