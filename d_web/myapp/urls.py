from django.conf.urls import patterns, include, url

from . import views

urlpatterns = [
        url(r'^$', views.hello, name='index'),
        url(r'^hello', views.hello, name='hello'),
        url(r'^bye/', views.bye, name='bye'),
        url(r'^articles/(d{2})/(d{4})/', views.viewArticles, name='articles'),
        url(r'^crudops/', views.crudops, name='crudops'),
        url(r'^static/', views.static, name='static')
    ]
