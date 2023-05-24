from django.contrib import admin
from .models import User, Types, Tasks, Colors


class ColorAdmin(admin.ModelAdmin):
    list_display = ('id', "color")
    list_display_links = ('id', "color")


admin.site.register(Colors, ColorAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', "type")
    list_display_links = ('id', "type")


admin.site.register(Types, TypeAdmin)



class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', "descr", "dateTask", "color", "type", "datenotif", "reminder")
    list_display_links = ('id', "descr", "dateTask", "color", "type", "datenotif", "reminder")


admin.site.register(Tasks, TaskAdmin)




# Register your models here.
