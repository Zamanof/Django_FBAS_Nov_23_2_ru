from django.contrib import admin
from . import models

admin.site.site_title = "ToDoApp Admin Panel"
admin.site.site_header = "ToDoApp Admin Panel"
admin.site.index_title = "Welcome to ToDoApp Admin Panel"

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates',{
            'fields': ['created'],
            'classes':['collapse']
        })
    ]



admin.site.register(models.Category)
admin.site.register(models.Task)
