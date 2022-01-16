from django.contrib import admin

from .models import Client, Profile,ProfileJson

# Register your models here.

admin.site.register(Client)
admin.site.register(Profile)
admin.site.register(ProfileJson)
