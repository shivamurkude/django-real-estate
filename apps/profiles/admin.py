from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display=["id","pkid","user","gender","phone_number","country","city"]
    list_filter=["gender","city","country"]
    list_display_links=["id","pkid","user"]

admin.site.register(Profile, ProfileAdmin)
