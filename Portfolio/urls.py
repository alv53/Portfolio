from django.conf.urls import patterns, include, url
from django.contrib import admin
from myportfolio.views import hello
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello)
)
