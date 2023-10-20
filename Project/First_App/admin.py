from django.contrib import admin

# Register your models here.
from First_App.models import Contact

class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'email','subject', 'message']


admin.site.register(Contact, AdminContact)




# user name:  arafat
# pass: 1234