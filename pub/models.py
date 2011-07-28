from django.db import models

# Create your models here.
class codes(models.Model):	
	owner = models.CharField(max_length=100)
	code = models.TextField()
	
	def __str__(self):
		return self.owner
	
	class Admin():
		pass
