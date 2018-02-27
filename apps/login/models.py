from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

# Create your models here.
class UserManager(models.Manager):
	def basic_validator(self, postData):
		name_regex = re.compile(r'^[a-zA-Z]+$')
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = {}
		if len(postData['fname']) < 2:
			errors['fname'] = 'First name field should be more than 2 characters!'
		if len(postData['lname']) < 2:
			errors['lname'] = 'Last name field should be more than 2 characters!'
		if not name_regex.match(postData['fname']) or not name_regex.match(postData['lname']):
			errors['letters'] = 'Letters only for names please'
		if not EMAIL_REGEX.match(postData['email']):
			errors['email'] = 'Invalid email address!'
		if len(postData['pword']) < 8:
			errors['pword'] = 'Password too short'
		if not postData['pword'] == postData['cpword']:
			errors['cpword'] = 'Passwords dont match'
		if User.objects.filter(email = postData['email'].lower()).exists():
			errors['exists'] = 'Email already used'
		if len(errors) == 0:
			pw = bcrypt.hashpw(postData['pword'].encode(), bcrypt.gensalt())
			a = User.objects.create(fname = postData['fname'], lname = postData['lname'],
				email= postData['email'].lower(), pword = pw)
			errors['a'] = postData['fname']
		return errors

	def login_validator(self,postData):
		EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
		errors = {}
		if len(postData['email']) < 1:
			errors['email'] = 'Email field left blank!'
		if len(postData['pword1']) < 1:
			errors['pword1'] = 'Password field left blank!'
		if len(errors) == 0:
			if User.objects.filter(email = postData['email']).exists():
				a = User.objects.get(email = postData['email'])
				if bcrypt.checkpw(postData['pword1'].encode(), a.pword.encode()):
					errors['a'] = a.fname
				else:
					errors['credentials'] = "Wrong Credentials"
			else:
				errors['credentials'] = "Wrong Credentials"
		return errors
class User(models.Model):
	"""docstring for User"""
	fname = models.CharField(max_length = 255)
	lname = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	pword = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()