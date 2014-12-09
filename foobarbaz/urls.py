from django.conf import settings
from django.conf.urls import patterns, url, include

# RESTful stuffs
from tastypie.api import Api
from foobarbaz.api import ModelItem
#from django.views.generic import TemplateView
from foobarbaz.views import views

v1_api = Api(api_name='v1')
v1_api.register(ModelItem())

urlpatterns = patterns('',
    #url(r'^foo$', views.foo, name='foo'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^$', views.index, name='index'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
