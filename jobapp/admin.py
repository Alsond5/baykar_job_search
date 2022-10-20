from django.contrib import admin
from .models import Job, Applicants

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'status', 'created_on')
    search_fields = ['title', 'description', 'department']
    list_filter = ('status','country')
    prepopulated_fields = {'slug': ('title',)}

class ApplicantsAdmin(admin.ModelAdmin):
    list_display = ('job', 'user')
    search_fields = ['job', 'user']
    list_filter = ('job',)

admin.site.register(Job, JobAdmin)
admin.site.register(Applicants, ApplicantsAdmin)