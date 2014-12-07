from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView


urlpatterns = patterns('',
    #url(r'^foo$', views.foo, name='foo'),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
