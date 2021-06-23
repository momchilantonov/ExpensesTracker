from django.contrib import admin

from expenses_tracker.tracker.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', "budget"]
