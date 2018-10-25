from django.contrib import admin
from .models import project_list
from .models import module
# Register your models here.

class projectadmin(admin.ModelAdmin):
    list_display = ['name', 'describe','status', 'create_time','update_time','id']
class modeadmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time','id']
admin.site.register(project_list,projectadmin)
admin.site.register(module,modeadmin)
