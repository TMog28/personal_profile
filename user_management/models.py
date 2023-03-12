from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .registration import UserManager
# # Create your models here.


class User(AbstractUser):
	username = None #remove username field will  be using email fields
	email = models.EmailField(_('email address'), unique=True)
	date_of_birth   = models.DateField(null=True, blank=True)
	gender          = models.CharField(max_length=250,null=True, blank=True)
	citizenship     = models.CharField(max_length=250,null=True, blank=True)
	contact_cell    = models.CharField(max_length=250,null=True, blank=True)
	bio 			      = models.TextField(null=True, blank=True)
	profile_photo   = models.ImageField(upload_to = 'profiles', default = 'imgs/avatar.png')
	job_title				= models.CharField(max_length=500,null=True, blank=True)
	home_address 		= models.TextField(null=True, blank=True)
	location				= models.CharField(max_length=500,null=True, blank=True)
	user_lat				= models.CharField(max_length=500,null=True, blank=True)
	user_lon				= models.CharField(max_length=500,null=True, blank=True)
	
	USERNAME_FIELD = 'email'
	EMAIL_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = UserManager()
