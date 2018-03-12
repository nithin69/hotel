from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from hbooking import views, models


urlpatterns = [
    # Examples:
    # url(r'^$', 'hotel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('hbooking.urls')),
    url(r'^review/', include('review.urls')),
    #url(r'^jet/', include('jet.urls', 'jet')),
    #url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]



if settings.DEBUG:
        urlpatterns += patterns(
                'django.views.static',
                (r'media/(?P<path>.*)',
                'serve',
                {'document_root': settings.MEDIA_ROOT}), )
