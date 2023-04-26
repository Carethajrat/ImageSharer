from django.contrib import admin
from .models import Post,ContactUs

class PostAdmin(admin.ModelAdmin):
    pass
class ContactUsAdmin(admin.ModelAdmin):
    pass

admin.site.register(Post,PostAdmin)
admin.site.register(ContactUs,ContactUsAdmin)
