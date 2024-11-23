from django.contrib import admin
from .models import Contact,Project
# Register your models here.

@admin.register(Contact)
class ContactAdminModel(admin.ModelAdmin):
    list_display=['id','name','email','phonenumber','description']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section', 'github_link', 'timestamp']
    search_fields = ['name', 'section']
    list_filter = ['section', 'timestamp']

