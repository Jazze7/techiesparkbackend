from django.contrib import admin
from web.models import Event,MomentGallery


class MomentGalleryAdmin(admin.TabularInline):
    list_display=('id','image')
    model=MomentGallery


class EventAdmin(admin.ModelAdmin):
    list_display=('id','title','date')
    inlines=[MomentGalleryAdmin]

admin.site.register(Event,EventAdmin)







