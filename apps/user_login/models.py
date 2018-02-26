from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user(models.Model):
	"""docstring for user"""
	first_name = models.CharField(max_length = 255)
	last_name = models.CharField(max_length = 255)
	email_address = models.CharField(max_length = 255)
	age = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add = True)
	Updated_at = models.DateTimeField(auto_now = True)
		