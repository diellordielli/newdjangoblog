from django.conf.urls.defaults import patterns, include, url
from blogengine.views import PostsFeed
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import ListView
from blogengine.models import Category, Post
from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # Home page
    url(r'^(?P<page>\d+)?/?$', 'blogengine.views.home'),

    # Blog Posts
    url(r'^\d{4}/\d{1,2}/(?P<postSlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getPost'),

    # Categories
    url(r'^categories/?$', ListView.as_view(model = Category)),
    url(r'^categories/(?P<categorySlug>[-a-zA-Z0-9]+)/?$', 'blogengine.views.getCategory', name = "category_detail"),

    # Comments
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    # Tags
  
    # Archive
    (r"^month/(\d+)/(\d+)/$", "month"),

    # RSS feeds
    url(r'^feeds/posts/$', PostsFeed()),

)

urlpatterns += staticfiles_urlpatterns()
