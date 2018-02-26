from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
	return render(request, 'login/index.html')

def create(request):
	if request.method == "POST":
		errors = User.objects.basic_validator(request.POST)
		if len(errors):
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/login')
		else:
			pw = bcrypt.hashpw(request.POST['pword'].encode(), bcrypt.gensalt())
			User.objects.create(fname = request.POST['fname'], lname = request.POST['lname'],
				email= request.POST['email'].lower(), pword = pw)
			request.session['id'] = request.POST['fname']
	return redirect('/login/log')

def login(request):
	return render(request, 'login/success.html')

def log(request):
	if request.method == "POST":
		b = request.POST['email']
		if User.objects.filter(email = b).exists():
			a = User.objects.get(email = b)
			request.session['id'] = a.fname
			if bcrypt.checkpw(request.POST['pword1'].encode(), a.pword.encode()):
				return redirect('/login/log')
			else:
				messages.add_message(request, messages.INFO, 'Wrong Password')
				return redirect('/login')
		else:
			messages.add_message(request, messages.INFO, 'Invalid Email')
			return redirect('/login')
	return redirect('/login')





