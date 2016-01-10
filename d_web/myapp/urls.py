from django.conf.urls import patterns, include, url

urlpatterns = patterns(
        'myapp.views',
        url(r'^hello/', 'hello', name='hello'),
        url(r'^bye/', 'bye', name='bye'),
        url(r'^articles/(d{2})/(d{4})/', 'viewArticles', name='articles'),
        url(r'^crudops/', 'crudops', name='crudops'),
        url(r'^static/', 'static', name='static')
    )
