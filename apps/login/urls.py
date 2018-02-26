from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
	url(r'^$', views.index),     # This line has changed!
	url(r'^/create$', views.create),
	url(r'^/log$', views.login),
	url(r'^/logg$', views.log)
]