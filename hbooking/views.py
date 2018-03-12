from django.shortcuts import render
from django.template import RequestContext
from hbooking.forms import *
from django.shortcuts import render_to_response, get_object_or_404
from django.db.models import Q
from django.core.mail import send_mail, EmailMessage
import hashlib
from random import randint
from django.views.decorators.csrf import csrf_protect, csrf_exempt
#from django.core.context_processors import csrf
from datetime import date
from dateutil.parser import parse
import urllib, urllib2
from django.utils import translation
from django import http
from django.conf import settings
from datetime import datetime
import calendar

date_format = "%d-%m-%Y"

user_language = 'en'
translation.activate(user_language)
# Create your views here.


def index(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    bastar = Room.objects.filter(location=location)
    
    print request    
    context_dict = {'bastar':bastar, 'location':location,}
    return render(request, 'hotel-templates/index.html', context_dict)


def about(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    about = About.objects.filter(location=location)
    context_dict = {'about':about, 'location':location}
    return render(request, 'hotel-templates/about.html', context_dict)



def landing(request):
    context_dict = {}
    return render(request, 'hotel-templates/landing.html', context_dict)


def facilities(request, slug):
    context_dict = {}
    l = Location.objects.get(slug=slug)
    facility = Facility.objects.filter(location=l)
    context_dict = {'facility':facility, 'l':l}
    return render(request, 'hotel-templates/facilities.html', context_dict)


def gallery(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    gallery = Gallery.objects.filter(location=location)
    context_dict = {'gallery': gallery, 'location':location}
    return render(request, 'hotel-templates/gallery.html', context_dict)

def namanbastar(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    room = Room.objects.filter(location=location)
    context_dict = {'room':room, 'location':location}
    return render(request, 'hotel-templates/rooms.html', context_dict)

def namanheight(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    room = Room.objects.filter(location=location)
    
    context_dict = {'room':room, 'location':location}
    return render(request, 'hotel-templates/namanheight.html', context_dict)


def tours(request, slug):
    context_dict = {}
    location = Location.objects.get(slug=slug)
    tours = Spiritual_tours.objects.get(location=location)
    context_dict = {'tours':tours}
    return render(request, 'hotel-templates/tours.html', context_dict)


def contact(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        mobiles = request.POST['phone']
        #print "request post : ", request.POST
        if contact_form.is_valid():
            authkey = "144560AtNwgJSU58c2e32e"
            url = "http://sms.rpsms.in/api/sendhttp.php"
            sender = "ambdkr"
            route = 1
            message1 = " Thank You for contacting Naman Bastar. We will get back to you shortly."
       		 # Prepare you post parameters
            values = {
                  'authkey' : authkey,
                  'mobiles' : mobiles,
                  'message' : message1,
                  'sender' : sender,
                  'route' : route
                  }

            postdata = urllib.urlencode(values) # URL encoding the data here.
            req = urllib2.Request(url, postdata)
            response = urllib2.urlopen(req)
            output = response.read()
            contact = contact_form.save()
            done = True
        else:
            "sorry "
            print contact_form
    else:
        contact_form = ContactForm()
    
    
    return render_to_response('hotel-templates/contact.html',
     {'contact_form': contact_form,
     'done': done}, context)


def contact_height(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        mobiles = request.POST['phone']
        #print "request post : ", request.POST
        if contact_form.is_valid():
            authkey = "144560AtNwgJSU58c2e32e"
            url = "http://sms.rpsms.in/api/sendhttp.php"
            sender = "ambdkr"
            route = 1
            message1 = " Thank You for contacting Naman Heights. We will get back to you shortly."
       		 # Prepare you post parameters
            values = {
                  'authkey' : authkey,
                  'mobiles' : mobiles,
                  'message' : message1,
                  'sender' : sender,
                  'route' : route
                  }

            postdata = urllib.urlencode(values) # URL encoding the data here.
            req = urllib2.Request(url, postdata)
            response = urllib2.urlopen(req)

            output = response.read()
            contact = contact_form.save()
            done = True
        else:
            "sorry "
            print contact_form
    else:
        contact_form = ContactForm()
    
    
    return render_to_response('hotel-templates/contact_height.html',
     {'contact_form': contact_form,
     'done': done}, context)



def bastar(request):
    context_dict = {}
    return render(request, 'hotel-templates/bastar.html', context_dict)


def height(request):
    context_dict = {}
    return render(request, 'hotel-templates/heights.html', context_dict)



'''
def booking(request):
    
    context = RequestContext(request)
    done = False
    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)
        #print "request post : ", request.POST
        if booking_form.is_valid():
	    from_email = ['contact@namanbastar.com']
	    email = request.POST['email']
            message = request.POST['message']
	    print email
            send_mail('Room Booking', message, from_email, [email], fail_silently=False)
            booking = booking_form.save()
            done = True
    
        else:
            "sorry "
            print booking_form
    else:
        booking_form = BookingForm()
    
    
    return render_to_response('hotel-templates/booking.html',
     {'booking_form': booking_form,
     'done': done}, context)
'''

def search(request, slug):
    
    context = RequestContext(request)
     
  	
    if 'arrival_date' in request.GET:
        arrival_date = request.GET['arrival_date']
    
    if 'departure_date' in request.GET:
        departure_date = request.GET['departure_date']

    if 'room' in request.GET:
	room = request.GET['room']

	
    if 'no_of_rooms' in request.GET:
	no_of_rooms = int(request.GET['no_of_rooms'])

    if 'adults' in request.GET:
	adults = request.GET['adults']
    

    booked = set(values['room_type_id'] for values in Booking.objects.filter(
    arrival_date__lte=arrival_date, departure_date__gte=arrival_date, no_of_rooms__gt=no_of_rooms, adults=adults).values('room_type_id'))
    
    booking_search = Room.objects.exclude(id__in=booked).filter(id=room)
    room = Room.objects.get(id=booking_search)
    arrival_date = arrival_date.replace('/', '-')
    departure_date = departure_date.replace('/', '-')

    if (int(no_of_rooms) <= int(room.available_rooms)):
    	
	print "Book now", type(no_of_rooms)
    
    else:

	print "Sorry", type(no_of_rooms)	
    print slug

    return render_to_response('hotel-templates/search.html', {'booking_search': booking_search,'arrival_date':arrival_date, 'departure_date':departure_date,"no_of_rooms":no_of_rooms, 'adults':adults}, context)




def booking(request, slug, arrival_date, departure_date, no_of_rooms):

    	context = RequestContext(request)
        MERCHANT_KEY = "fVDG2I4M"
	key="fVDG2I4M"
	SALT = "U5PdBSp4J1"
	PAYU_BASE_URL = "https://secure.payu.in/_payment"
	action = ''
	posted={}
	for i in request.POST:
		posted[i]=request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid']=txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key']=key
	hash_string=''
	hashVarsSeq=hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string+=str(posted[i])
		except Exception:
			hash_string+=''
		hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	action =PAYU_BASE_URL
        print "arrival_date", arrival_date
	print "departure_date", departure_date
	room = Room.objects.get(slug=slug)
        a = datetime.strptime(arrival_date, date_format)
	b = datetime.strptime(departure_date, date_format)
	delta = b - a
        print "dates are " , delta
	no_of_days =  delta.days
	
	print "no_of_days", no_of_days
 	rate = Rate.objects.filter(date__range=[a, b], room_type = room.id)[:no_of_days]
	print rate
	amount = 0
	for i in rate:
		amount += int(i.rate)
	
	no_of_days = int(no_of_days)
	room_rate =  int(no_of_rooms)
	try:
		sum_amount = int(amount)/no_of_days
		amount =  sum_amount*room_rate*no_of_days
  	except ZeroDivisionError:

		sum_amount = int(amount)
		amount =  sum_amount*room_rate
	
	print "amount", amount
	if amount >= 2500:

		gst = amount *18/100

	else:

		gst = amount *12/100

	print "gst is",gst

	total_amount = gst + amount
	context = RequestContext(request)
    	done = False
    	if request.method == "POST":
        	booking_form = BookingForm(data=request.POST)
        	if booking_form.is_valid():
	    		from_email = 'vishnu@delevere.com'
	    		email = request.POST['email']
            		message = "Dear Patrons,\n\n  Greetings from Naman Bastar!!\n\n We would like to thank you for choosing our portal for executing your travel plans.Please be informed that our travel site is backed by a team of experienced people who have been in travel trade for many years.\n\n Please refer to the various guidelines we have mentioned on the vouchers. We would again request you to please carry some photo identification proof along with you while travelling. In case of any emergency you may contact the Hotel / Resort directly referring your 'BOOKING reference number'  or otherwise can contact our Manager on duty  at +91-7782-229740\n\n Once again thank you for your support and wish you a very happy and pleasant stay.\n\n  namanbastar.com,\nNAMAN BASTAR Chitrakote Road,\n Village Palli,JagdalPur,\n Chattisgarh, pincode: 494001,\n+91-7782-229740"
			amount = request.POST['amount']
			
            		s = EmailMessage('Room Booking', message, from_email, [email])
			s.attach_file('/home/rtxing8/webapps/static/hotel-static/pdf/cancel.pdf', "application/pdf")
			s.attach_file('/home/rtxing8/webapps/static/hotel-static/pdf/policy.pdf', "application/pdf")
			s.send()
            		booking = booking_form.save()
            		done = True
    
        	else:
            		"sorry "
            		print booking_form
    	else:
        	booking_form = BookingForm()	


	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
		return render_to_response('hotel-templates/booking.html',RequestContext(request,{"posted":posted, "arrival_date":arrival_date, "departure_date":departure_date, "amount":amount,"gst":gst,"total_amount":total_amount,"room":room, "no_of_rooms":no_of_rooms, "booking_form":booking_form, "done":done, "hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://secure.payu.in/_payment" }))
	else:
		return render_to_response('hotel-templates/booking.html',RequestContext(request,{"posted":posted, "arrival_date":arrival_date, "departure_date":departure_date,"gst":gst,"total_amount":total_amount, "no_of_rooms":no_of_rooms,"room":room, "booking_form":booking_form, "done":done, "amount":amount,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":".", "slug":slug }))





def booking_heights(request, slug, arrival_date, departure_date, no_of_rooms, adults):
	
        MERCHANT_KEY = "fVDG2I4M"
	key="fVDG2I4M"
	SALT = "U5PdBSp4J1"
	PAYU_BASE_URL = "https://secure.payu.in/_payment"
	action = ''
	posted={}
	for i in request.POST:

		posted[i]=request.POST[i]
	hash_object = hashlib.sha256(b'randint(0,20)')
	txnid=hash_object.hexdigest()[0:20]
	hashh = ''
	posted['txnid']=txnid
	hashSequence = "key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10"
	posted['key']=key
	hash_string=''
	hashVarsSeq=hashSequence.split('|')
	for i in hashVarsSeq:
		try:
			hash_string+=str(posted[i])
		except Exception:
			hash_string+=''
		hash_string+='|'
	hash_string+=SALT
	hashh=hashlib.sha512(hash_string).hexdigest().lower()
	action =PAYU_BASE_URL
        print "arrival_date", arrival_date
	print "departure_date", departure_date
	room = Room.objects.get(slug=slug)
        a = datetime.strptime(arrival_date, date_format)
	b = datetime.strptime(departure_date, date_format)
	delta = b - a
        print "dates are " , delta
	no_of_days =  delta.days
	if(a == b):
	    no_of_days = 1
	print "no_of_days", no_of_days
	print "no of rooms", no_of_rooms
	print "adults", adults
 	rate = Rate.objects.filter(date__range=[a, b], room_type = room.id)[:no_of_days]
	print rate
	amount = 0
	if adults == adults:
		for i in rate:
			amount+= int(i.rate)
	
		no_of_days = int(no_of_days)
		room_rate =  int(no_of_rooms)
		try:
			sum_amount = int(amount)/no_of_days
			amount =  sum_amount*room_rate*no_of_days
			print "amount", amount
  		except ZeroDivisionError:

			sum_amount = int(amount)
			amount =  sum_amount*room_rate
	
		if amount >= 2500:

			gst = amount *18/100

		else:

			gst = amount *12/100

		print "gst is",gst

		total_amount = gst + amount

		print "gst is",gst
	else:

		for i in rate:
			amount+= int(i.rate2)
	
		no_of_days = int(no_of_days)
		room_rate =  int(no_of_rooms)
		try:
			sum_amount = int(amount)/no_of_days
			amount =  sum_amount*room_rate*no_of_days
  		except ZeroDivisionError:

			sum_amount = int(amount)
			amount =  sum_amount*room_rate
	
		if amount >= 2500:

			gst = amount *18/100

		else:

			gst = amount *12/100

		print "gst is",gst

		total_amount = gst + amount

		print "gst is",gst

	context = RequestContext(request)
    	done = False
    	if request.method == "POST":
        	booking_form = BookingForm(data=request.POST)
        	if booking_form.is_valid():
	    		from_email = 'vishnu@delevere.com'
	    		email = request.POST['email']
            		message = "Dear Patrons,\n\n  Greetings from Naman Heights!!\n\n We would like to thank you for choosing our portal for executing your travel plans.Please be informed that our travel site is backed by a team of experienced people who have been in travel trade for many years.\n\n Please refer to the various guidelines we have mentioned on the vouchers. We would again request you to please carry some photo identification proof along with you while travelling. In case of any emergency you may contact the Hotel / Resort directly referring your 'BOOKING reference number'  or otherwise can contact our Manager on duty  at +91-07782-231355\n\n Once again thank you for your support and wish you a very happy and pleasant stay.\n\n  namanheights.com,\nAghanpur, Dharampura Road,\n JagdalPur 494001 Chattisgarh,\n+91-07782-231355"
			amount = request.POST['amount']
		
         	        s = EmailMessage('Room Booking', message, from_email, [email])
                        s.attach_file('/home/rtxing8/webapps/static/hotel-static/pdf/cancel.pdf', "application/pdf")
                        s.attach_file('/home/rtxing8/webapps/static/hotel-static/pdf/policy.pdf', "application/pdf")
                        s.send()

            		booking = booking_form.save()
            		done = True
    
        	else:
            		"sorry "
            		print booking_form
    	else:
        	booking_form = BookingForm()	

	if(posted.get("key")!=None and posted.get("txnid")!=None and posted.get("productinfo")!=None and posted.get("firstname")!=None and posted.get("email")!=None):
		return render_to_response('hotel-templates/booking_heights.html',RequestContext(request,{"posted":posted, "arrival_date":arrival_date, "departure_date":departure_date, "amount":amount,"gst":gst,"total_amount":total_amount,"room":room, "no_of_rooms":no_of_rooms,"booking_form":booking_form, "done":done,  "hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":"https://secure.payu.in/_payment" }))
	else:
		return render_to_response('hotel-templates/booking_heights.html',RequestContext(request,{"posted":posted, "arrival_date":arrival_date, "departure_date":departure_date,"gst":gst,"total_amount":total_amount, "no_of_rooms":no_of_rooms,"room":room,"booking_form":booking_form, "done":done, "amount":amount,"hashh":hashh,"MERCHANT_KEY":MERCHANT_KEY,"txnid":txnid,"hash_string":hash_string,"action":".", "slug":slug }))



def single_room(request, slug, arrival_date, departure_date):
    context_dict = {}
    single = Room.objects.get(slug=slug)
    print "ad", arrival_date   
    context_dict = {'single':single, 'arrival_date':arrival_date, 'departure_date':departure_date}
    return render(request, 'hotel-templates/platinumroom.html', context_dict)





def dashboard_home(request):
    context_dict = {}
    rooms = Room.objects.all()
    context_dict = {'rooms':rooms}
    return render_to_response('hotel-templates/dashboard_search.html', context_dict)


def dashboard(request):
    
    context = RequestContext(request)
     
    if 'month' in request.GET:
        month = int(request.GET['month'])

    if 'year' in request.GET:
        year = int(request.GET['year'])

    if 'room_type' in request.GET:
        room_type = request.GET['room_type']
       
    num_days = calendar.monthrange(year, month)[1]

    days = [[date(year, month, day)] for day in range(1, num_days+1)]

    
    for day in days:
    	rates = Rate.objects.filter(room_type=room_type, date=str(day[0]))
	room = Room.objects.filter(id=room_type)
	for a in room:
		quantity =  a.available_rooms
		title= a.title
        	day.append(rates)
		day.append(quantity)
		day.append(a)
		
    for i in days:
        print i
    rooms = Room.objects.all()
    return render_to_response('hotel-templates/dashboard.html', {'rooms':rooms,'rates':rates,'days':days}, context)


@csrf_protect
@csrf_exempt
def success(request):
	c = {}
    	c.update(csrf(request))
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="Cx5nEdgiUz"
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."
	return render_to_response('hotel-templates/sucess.html',RequestContext(request,{"txnid":txnid,"status":status,"amount":amount}))


@csrf_protect
@csrf_exempt
def failure(request):
	c = {}
    	c.update(csrf(request))
	status=request.POST["status"]
	firstname=request.POST["firstname"]
	amount=request.POST["amount"]
	txnid=request.POST["txnid"]
	posted_hash=request.POST["hash"]
	key=request.POST["key"]
	productinfo=request.POST["productinfo"]
	email=request.POST["email"]
	salt="Cx5nEdgiUz"
	try:
		additionalCharges=request.POST["additionalCharges"]
		retHashSeq=additionalCharges+'|'+salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	except Exception:
		retHashSeq = salt+'|'+status+'|||||||||||'+email+'|'+firstname+'|'+productinfo+'|'+amount+'|'+txnid+'|'+key
	hashh=hashlib.sha512(retHashSeq).hexdigest().lower()
	if(hashh !=posted_hash):
		print "Invalid Transaction. Please try again"
	else:
		print "Thank You. Your order status is ", status
		print "Your Transaction ID for this transaction is ",txnid
		print "We have received a payment of Rs. ", amount ,". Your order will soon be shipped."
 	return render_to_response("hotel-templates/Failure.html",RequestContext(request,c))




def room_view(request, slug, location):
    
    context = RequestContext(request)
    

    single = Room.objects.get(slug=slug)
    
    
    done = False
    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        #print "request post : ", request.POST
        if review_form.is_valid():
	    from_email = ['vishnu@delevere.com']
	    email = request.POST['email']
            comment = request.POST['comment']
  	    room_type_id = single.id
	    print room_type_id
	    print email
            
            review = review_form.save()
            done = True
    
        else:
            "sorry "
            print review_form
    else:
        review_form = ReviewForm()

    review = Review.objects.filter(room_type = single.id, status="Approve")
    print review
    return render_to_response('hotel-templates/platinumroom.html',
     {'review_form': review_form,
     'done': done, 'single':single, 'review':review}, context)
	
