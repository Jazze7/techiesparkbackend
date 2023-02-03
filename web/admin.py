from django.contrib import admin
from web.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=('id','title','date')
admin.site.register(Event,EventAdmin)