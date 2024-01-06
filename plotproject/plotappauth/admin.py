from django.contrib import admin

from .models import ResetPassword


# admin.site.register(ResetPassword)
@admin.register(ResetPassword)
class Mylisting(admin.ModelAdmin):
    list_display = ('old_password', 'new_password', 'confirm_password')
