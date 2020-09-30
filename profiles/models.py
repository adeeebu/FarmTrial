from django.db import models

class FarmerProfile(models.Model):
	fname = models.CharField(max_length = 30)
	lname = models.CharField(max_length = 30)
	email = models.EmailField(max_length = 50)
	dist = models.CharField(max_length = 30)
	state = models.CharField(max_length = 30)
	passwd = models.CharField(max_length = 30)

	def __str__(self):
		return self.lname + ', ' + self.fname





# Create your models here.
