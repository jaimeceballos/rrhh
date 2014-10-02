from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'rrhh.views.home', name='home'),
    # url(r'^rrhh/', include('rrhh.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'apps.accounts.views.login', name='login'),
    url(r'^$', 'apps.accounts.views.logout', name='logout'),
    url(r'^personal/', include('apps.personal.urls')),
    url(r'^referencias/', include('apps.referencias.urls')),
)