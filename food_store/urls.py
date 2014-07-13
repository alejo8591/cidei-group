from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'food_store.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
# URLs for Media files for Develop
if settings.DEBUG:
	urlpatterns+= patterns(
		'django.views.static',
		(r'media/(?P<path>.*)',
		'serve',
		{'document_root' : settings.MEDIA_ROOT}), 
	)	