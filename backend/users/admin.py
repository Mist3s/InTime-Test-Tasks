from django.contrib import admin

from .models import User, AuthCode


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'last_name',
        'first_name'
    )
    list_filter = ('email',)
    search_fields = ('last_name', 'first_name', 'email')


@admin.register(AuthCode)
class AuthCodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'code',
        'user',
        'datetime_end',
        'used'
    )
