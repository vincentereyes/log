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
		if 'a' not in errors:
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/login')
		else:
			request.session['id'] = errors['a']
			return redirect('/login/log')
	return redirect('/login')

def login(request):
	return render(request, 'login/success.html')

def log(request):
	if request.method == "POST":
		errors = User.objects.login_validator(request.POST)
		if 'a' not in errors:
			for tag, error in errors.iteritems():
				messages.error(request,error, extra_tags = tag)
			return redirect('/login')
		else:
			request.session['id'] = errors['a']
			return redirect('/login/log')
	return redirect('/login')





