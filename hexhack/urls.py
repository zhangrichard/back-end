from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hexhack.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^touchtable/', include('touchtable.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
