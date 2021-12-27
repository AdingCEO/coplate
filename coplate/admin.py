from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review

# Register your models here.
admin.site.register(User, UserAdmin)

#Users 모델에 대한 추가필드는 따로 어드민페이지에 나오지 않기때문에 어드민 페이지에 나오도록 추가
UserAdmin.fieldsets += (("Custom fields", {"fields":("nickname", 'profile_pic', 'intro')}),)

admin.site.register(Review)