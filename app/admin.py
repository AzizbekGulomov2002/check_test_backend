from django.contrib import admin
from .models import *
# Register your models here.
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['t_id','name','language','date']
    list_filter = ['created']
    search_fields = ['t_id','name','surname']
    list_per_page = 10
admin.site.register(BotUser,BotUserAdmin)
class TestAdmin(admin.ModelAdmin):
    list_display = ['code','creator','created','status']
    list_filter = ['created','code']
    list_per_page = 10
    search_fields = ['code']
admin.site.register(Test,TestAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['username','result']
    list_per_page = 10
    search_fields = ['result','user__name']
admin.site.register(Student,StudentAdmin)