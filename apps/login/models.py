from __future__ import unicode_literals
import re
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
		return errors
class User(models.Model):
	"""docstring for User"""
	fname = models.CharField(max_length = 255)
	lname = models.CharField(max_length = 255)
	email = models.CharField(max_length = 255)
	pword = models.CharField(max_length = 255)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()