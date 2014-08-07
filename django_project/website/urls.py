from django.conf.urls import patterns, include, url


urlpatterns = patterns('',    
    url(r'^$', 'website.views.home', name='home'),
    url(r'^info/$', 'website.views.info', name='info'),
    url(r'^map/get-apartments/$', 'website.views.get_apartments', name='get-apartments'),
    url(r'^map/apartments/filter/$', 'website.views.apartments_filter', name='apartments_filter'),
)
