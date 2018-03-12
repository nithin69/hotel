__author__ = 'rt'

from django.conf.urls import url, include#, patterns
from hbooking import views

urlpatterns = ('',
                url(r'^$', views.landing, name='landing'),
               # url(r'^about/(?P<slug>\S+)/$', views.about, name='about'),
  		       # url(r'^home/(?P<slug>\S+)/$', views.index, name='index'),
               # url(r'^facilities/(?P<slug>[\w-]+)/$', views.facilities, name='facilities'),
               # url(r'^gallery/(?P<slug>[\w-]+)/$', views.gallery, name='gallery'),
               # url(r'^namanbastar/(?P<slug>[\w-]+)/$', views.namanbastar, name='namanbastar'),
    		   # url(r'^namanheight/(?P<slug>[\w-]+)/$', views.namanheight, name='namanheight'),
               # url(r'^tours/(?P<slug>[\w-]+)/$', views.tours, name='tours'),
               # url(r'^contact/naman-bastar/$', views.contact, name='contact'),
		#url(r'^contact/naman-heights/$', views.contact_height, name='contact_height'),
		#url(r'^dashboard_home/$', views.dashboard_home, name='dashboard_home'),
		#url(r'^dashboard/$', views.dashboard, name='dashboard'),
		
        #        url(r'^bastar/naman-bastar/$', views.bastar, name='bastar'),
		#url(r'^heights/naman-heights/$', views.height, name='height'),
		#url(r'^naman-bastar/(?P<slug>\S+)/booking/(?P<arrival_date>\S+)/(?P<departure_date>\S+)/(?P<no_of_rooms>\d+)/$', views.booking, name='booking'),

		#url(r'^naman-heights/(?P<slug>\S+)/booking/(?P<arrival_date>\S+)/(?P<departure_date>\S+)/(?P<no_of_rooms>\d+)-(?P<adults>\d+)/$', views.booking_heights, name='booking_heights'),

		#url(r'^search/(?P<slug>\S+)/$', views.search, name='search'),
		#url(r'^room/(?P<slug>\S+)/(?P<arrival_date>\S+)-(?P<departure_date>\S+)/$', views.single_room, name='single_room'),
		#url(r'^room/(?P<location>\S+)/(?P<slug>\S+)/$', views.room_view, name='room_view'),
		#url(r'^Success/',views.success),
    #		url(r'^Failure/',views.failure),
                       
                       		      
)
