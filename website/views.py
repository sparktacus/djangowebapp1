from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
	return render(request, 'index.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			"Message from " + message_name + "@" + message_email, # subject
			message, # message
			settings.EMAIL_HOST_USER, # from email
			['laurimakoko44@gmail.com'], # to email
			)

		return render(request, 'contact.html', {'message_name':message_name})

	else:
		return render(request, 'contact.html', {})

def signin(request):
	return render(request, 'signin.html',{})

def payment(request):
	return render(request, 'payment.html', {})

def about(request):
	return render(request, 'about.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def service(request):
	return render(request, 'service.html', {})


def appointment(request):
	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_date = request.POST['your-date']
		your_message = request.POST['your-message']

		'''
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']
'''
		# send an email
		appointment = "\nname: " + your_name + "\nPhone: " + your_phone + "\nDate: " + your_date + "\nSchedule: " + your_schedule + "\n\nMessage :\n" + your_message
		send_mail(
			"Appointment request from " + your_email, # subject
			appointment, # message
			settings.EMAIL_HOST_USER, # from email
			['laurimakoko44@gmail.com'], # to email
			)
        
		return render(request, 'appointment.html', {
			'your_schedule': your_schedule,
			'your_name': your_name,
			'your_phone': your_phone,
			'your_email': your_email,
			'your_address': your_address,
			'your_date': your_date,
			'your_message': your_message
			})

	else:
		return render(request, 'index.html', {})