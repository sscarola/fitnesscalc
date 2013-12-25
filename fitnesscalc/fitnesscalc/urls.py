from django.conf.urls import patterns, include, url

from django.contrib import admin
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'profiles.views.home'),
    (r'^accounts/login/$', login),
    (r'^accounts/logout/$', logout),
    (r'^accounts/register/$', 'accounts.views.register'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
