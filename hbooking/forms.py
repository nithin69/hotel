from django import forms
from hbooking.models import *


class BookingForm(forms.ModelForm):

 	class Meta:
 		model = Booking
		fields = ("__all__")


class ContactForm(forms.ModelForm):

 	class Meta:
 		model = Contact
		fields = ("__all__")


class ReviewForm(forms.ModelForm):



 	class Meta:

 		model = Review

		fields = ("name", 'phone', 'comment', 'email', 'room_type')
