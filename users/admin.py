from django.contrib import admin
from users.models import User

# Register your models here..
class UserAdmin(admin.ModelAdmin):
    list_display=['phone_number',"first_name",'otp']

admin.site.register(User,UserAdmin)