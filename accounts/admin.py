from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    # here we are inheriting user admin from django admin database so it will show default fileds in db
    # to change or show more fields we use list_display function here
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    
    # if you have multiple user then to show them in decending order we user ordering
    ordering = ('-date_joined',) # use , in tuple otherwise it will throw error
    # to set the passwords non editable in database
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
    

admin.site.register(User, CustomUserAdmin) 