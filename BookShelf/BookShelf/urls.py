"""
Definition of urls for BookShelf.
"""

from datetime import datetime
from django.conf.urls import patterns, url

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^register/$', 'app.views.register', name='register'),
    url(r'^register/success/$', 'app.views.register_success', name='register_success'),
    url(r'^shelf$', 'app.views.shelf', name='shelf'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
