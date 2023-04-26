from django import forms
from phonenumber_field.formfields import PhoneNumberField

# creating form in here for user to upload/post an image,that will further be saved in DB
class PostForm(forms.Form):
    image = forms.FileField()
    text = forms.CharField(label="Description")

class ContactUsForm(forms.Form):
    email = forms.EmailField(label="Email Address")
    mobile = PhoneNumberField(label="Mobile No")
    message = forms.CharField(widget=forms.Textarea,label="Your Message")

