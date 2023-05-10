from django.contrib import admin

from invites.models import Invite


@admin.register(Invite)
class ProfileAdmin(admin.ModelAdmin):
    pass
# Register your models here.

