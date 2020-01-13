from django.contrib import admin
from .models import *


class ThemeAdmin(admin.ModelAdmin):
    list_display = ['theme', 'rubric']
    list_filter = ['rubric']


class AdsAdmin(admin.ModelAdmin):
    list_display = ['title', 'rubric', 'theme']
    list_filter = ['theme', 'rubric']


admin.site.register(Ads, AdsAdmin)
admin.site.register(Theme, ThemeAdmin)
admin.site.register(Rubric)
