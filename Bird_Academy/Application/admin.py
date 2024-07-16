from django.contrib import admin

from .models import Bird, Song

# admin.py
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Bird

@admin.register(Bird)
class BirdAdmin(admin.ModelAdmin):
    list_display = ('Latin_name', 'Fr_name', 'Eng_name')
    filter_horizontal = ('User_Bird',)

class BirdInline(admin.TabularInline):
    model = Bird.User_Bird.through
    extra = 1

class UserAdmin(BaseUserAdmin):
    inlines = (BirdInline,)

# Unregister the original User admin and register the new User admin with the inline
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# admin.site.register(Bird)
admin.site.register(Song)

