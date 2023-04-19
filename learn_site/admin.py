from django.contrib import admin

from learn_site.models import Project, Task

# Register your models here.
@admin.register(Project)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Task)
class SettingAdmin(admin.ModelAdmin):
    list_display = ['name', 'status', 'priority', 'deadline', 'project']
