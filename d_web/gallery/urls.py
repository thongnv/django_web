from django.conf.urls import url

from . import views


app_name = 'gallery'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^slide/$', views.SlideView.as_view(), name='slide'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^img', views.ImageView.as_view(), name='image'),
]
