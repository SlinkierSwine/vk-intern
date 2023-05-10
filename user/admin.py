from django.contrib import admin

from user.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
