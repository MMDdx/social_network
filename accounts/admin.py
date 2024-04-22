from django.contrib import admin
from .models import Profile,Country

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', 'phone_number')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbr')
    search_fields = ('abbr',)


