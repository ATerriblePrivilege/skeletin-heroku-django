from django.conf import settings
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

# RESTful stuffs
from tastypie.api import Api
from foobarbaz.api import ModelItem

v1_api = Api(api_name='v1')
v1_api.register(ModelItem())

urlpatterns = patterns('',
    #url(r'^foo$', views.foo, name='foo'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
