from django.contrib import admin
from . models import *

# Register your models here.
class useradmin(admin.ModelAdmin):
    model = UserProfile

admin.site.register(UserProfile,useradmin)