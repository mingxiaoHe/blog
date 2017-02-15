from django.conf.urls import url
from blog.views import *

urlpatterns = [
    url(r'(\d*)^$', index, name='index'),
    url(r'^index/(\d*)',index, name = 'index'),
    url(r'^archive/(\w*)/(\d*)/(\d*)', archive, name='archive'),
    url(r'^article/$', article, name='article'),
    url(r'^about/$', about, name='about'),
    url(r'^category/(\w*)/(\d*)', category, name='category'),
    url(r'^tag/(\w*)/(\d*)', tag, name='tag'),
]