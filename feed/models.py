from django.db import models
from sorl.thumbnail import ImageField
from phonenumber_field.modelfields import PhoneNumberField
# creating model for our post
class Post(models.Model):
    text = models.CharField(max_length = 140,null = False,blank = False)
    image = ImageField()
    def __str__(self):
        return self.text


class ContactUs(models.Model):
    email = models.EmailField(unique=True,max_length = 140,null = False,blank = False)
    mobile = PhoneNumberField(unique=True,max_length=13,null=False,blank=False)
    message = models.TextField(null=False,blank=False)
    def __str__(self):
        return self.email


