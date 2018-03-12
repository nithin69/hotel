from django.db import models
from django.template.defaultfilters import slugify
# Create your models here.


class Location(models.Model):

    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique = True, null=True, blank=True)

    def __unicode__(self):
        return self.name




class Room(models.Model):
    available = "Available"
    not_available = "Not Available"
    status_choices = ((available, "Available"), (not_available, "Not Available"))
    title = models.CharField(max_length=255, null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    image1 = models.ImageField(upload_to = 'rooms', null=True, blank=True)
    image2 = models.ImageField(upload_to = 'rooms', null=True, blank=True)
    image3 = models.ImageField(upload_to = 'rooms', null=True, blank=True)
    image4 = models.ImageField(upload_to = 'rooms', null=True, blank=True)
    image5 = models.ImageField(upload_to = 'rooms', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    occupancy = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    view = models.CharField(max_length=255, null=True, blank=True)
    room_service = models.CharField(max_length=255, null=True, blank=True)
    terraces = models.CharField(max_length=255, null=True, blank=True)
    free_pickup_facilty = models.BooleanField(default=True)
    internet_free = models.BooleanField(default=True)
    gym = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    available_rooms = models.IntegerField(null=True, blank=True)
    arrival_date = models.CharField(max_length=255, null=True, blank=True)
    departure_date = models.CharField(max_length=255, null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    no_of_rooms = models.IntegerField(null=True, blank=True)
    no_of_days = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=40, choices = status_choices, null=True, blank=True)

    def save(self, *args, **kwargs):
	self.slug = slugify(self.title)
	super(Room, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_price(self):
	return self.rate


class Rate(models.Model):

    rate = models.IntegerField(null=True, blank=True, verbose_name = "Rate for one person")
    rate2 = models.IntegerField(null=True, blank=True, verbose_name = "Rate for two persons")
    date = models.DateTimeField(null=True, blank=True)
    room_type = models.ForeignKey('Room', null=True, blank=True)
    def __unicode__(self):
        return 'Rs %s ' % (self.rate)


class Bulk_rate(models.Model):

    room_type = models.ForeignKey('Room', null=True, blank=True)
    from_date = models.DateTimeField(null=True, blank=True)
    to_date = models.DateTimeField(null=True, blank=True)
    rate = models.IntegerField(null=True, blank=True, verbose_name = "Rate for one person")
    rate2 = models.IntegerField(null=True, blank=True, verbose_name = "Rate for two persons")

    def __unicode__(self):
        return 'Rs %s  (%s - %s - %s)' % (self.rate, self.from_date, self.to_date, self.room_type)


class Availability(models.Model):

    available = "Available"
    not_available = "Not Available"
    status_choices = ((available, "Available"), (not_available, "Not Available"))
    room = models.ForeignKey('Room') 
    arrival_date = models.CharField(max_length=40,null=True, blank=True)
    departure_date = models.CharField(max_length=40, null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)
    no_of_rooms = models.IntegerField(null=True, blank=True)
    no_of_days = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=40, choices = status_choices, null=True, blank=True)

    def __unicode__(self):
        return self.status   
 


class Booking(models.Model):
     # AutoField?

    
    key = models.CharField(max_length=10, null=True, blank=True)
    txnid = models.CharField(max_length=40, null=True, blank=True)
    amount = models.CharField(max_length=40, null=True, blank=True)
    firstname = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    productinfo = models.TextField(null=True, blank=True)
    surl = models.CharField(max_length=255, null=True, blank=True)
    furl = models.CharField(max_length=255, null=True, blank=True)
    hash_key = models.CharField(max_length=255, null=True, blank=True)
    udf1 = models.CharField(max_length=25, null=True, blank=True, verbose_name="City")
    udf2 = models.CharField(max_length=25, null=True, blank=True, verbose_name="Address")
    udf3 =models.CharField(max_length=25, null=True, blank=True,  verbose_name="State")
    udf4 = models.CharField(max_length=25, null=True, blank=True, verbose_name="Country")
    gstin_number = models.CharField(max_length=15, null=True, blank=True)
    registered_name = models.CharField(max_length=100, null=True, blank=True)
    udf5 = models.CharField(max_length=25, null=True, blank=True, verbose_name="Pincode")
    arrival_date = models.CharField(max_length=25, null=True, blank=True)
    departure_date = models.CharField(max_length=25, null=True, blank=True)
    adults = models.IntegerField(null=True, blank=True)
    no_of_rooms = models.IntegerField(null=True, blank=True)
    room_type = models.ForeignKey('Room', null=True, blank=True)
    def __unicode__(self):
        return self.email    

    class Meta:
        verbose_name_plural = 'Booking'



class Contact(models.Model):
     # AutoField?
    name = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=40, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Contact'


class Gallery(models.Model):
	
    title = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(upload_to = 'gallery', null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    def __unicode__(self):
        return self.title


class Facility(models.Model):
	
    title = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(upload_to = 'facility', null=True, blank=True)
    description = models.TextField(null=True, blank=True) 
    location = models.ForeignKey('Location', null=True, blank=True)
    def __unicode__(self):
        return self.title


class About(models.Model):

    title = models.CharField(max_length=40, null=True, blank=True)
    description_para1 = models.TextField(null=True, blank=True)
    description_para2 = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to = 'about', null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    def __unicode__(self):
        return self.title


class Spiritual_tours(models.Model):

    title = models.CharField(max_length=100, null=True, blank=True)
    description_para1 = models.TextField(null=True, blank=True)
    description_para2 = models.TextField(null=True, blank=True)
    description_para3 = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    image2 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    image3 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    image4 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    image5 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    image6 = models.ImageField(upload_to = 'spiritual', null=True, blank=True)
    location = models.ForeignKey('Location', null=True, blank=True)
    def __unicode__(self):
        return self.title

class Review(models.Model):

    approve = "Approve"

    deny = "Deny"

    status_choices = ((approve, "Approve"), (deny, "Deny"))	
    name =  models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    room_type=models.ForeignKey('Room', null=True, blank=True)
    status = models.CharField(max_length=40, choices = status_choices, null=True, blank=True)


    def __unicode__(self):

        return self.comment
