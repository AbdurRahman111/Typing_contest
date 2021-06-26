from django.contrib import admin
from .models import user_details, EmailConfirmed, add_contest
# Register your models here.

class EmailConfirmedAdmin(admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'activation_key', 'email_confirmed']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

admin.site.register(EmailConfirmed, EmailConfirmedAdmin)

admin.site.register(user_details)
admin.site.register(add_contest)