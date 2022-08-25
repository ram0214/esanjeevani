from django.contrib import admin

# Register your models here.
from mainapp.models import UserInfo


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display=["fullname", "email", "contact_no", "age", "problem"]


