from django.contrib import admin
from hbooking.models import *
# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    
    class Meta:
        model = Room
	list_display = ("title", "location", "rate", "image1", "image2", "image3", "image4", "image5")

admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Room, RoomAdmin)
admin.site.register(Gallery)
admin.site.register(Bulk_rate)
admin.site.register(Facility)
admin.site.register(Location)
admin.site.register(Rate)
admin.site.register(About)
admin.site.register(Spiritual_tours)
admin.site.register(Review)

