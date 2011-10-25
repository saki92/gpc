from django.conf.urls.defaults import patterns, include, url
from gpc.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
(r'^gpa/$',ip),
(r'^calc/$',calc),
#(r'^time/$',time),
(r'^final/$',value),
    # Examples:
    # url(r'^$', 'gpacalc.views.home', name='home'),
    # url(r'^gpacalc/', include('gpacalc.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
