from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class Contact(models.Model):
	name = models.CharField(max_length=30)
	phone = PhoneNumberField()
	email = models.EmailField(max_length=30)
	detail = models.TextField()

	def __str__(self):
		return self.email


class Blog(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    

    def __str__(self):
        return self.title