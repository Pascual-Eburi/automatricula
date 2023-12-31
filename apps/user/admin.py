
# Register your models here.
from django.contrib import admin

from . import models

from django.contrib.auth import get_user_model
User = get_user_model()

class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email','phone', 'rol','is_staff','is_superuser','is_active','last_login' )
    list_display_links = ('name', 'last_name', 'email', )
    search_fields = ('name', 'last_name', 'email','phone','rol','is_staff','is_superuser','is_active','last_login' )
    list_per_page = 25

admin.site.register(User, UserAdmin)