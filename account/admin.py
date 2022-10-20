from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'country', 'school', 'graduate_year','status')
    search_fields = ['user',]
    list_filter = ('status','country')

    prepopulated_fields = {'slug': ('user',)}

admin.site.register(Profile, ProfileAdmin)