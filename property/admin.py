from django.contrib import admin

from .models import Flat, Complait


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'floor', 'rooms_number', 'has_balcony')
    raw_id_fields = ("liked_by",)
admin.site.register(Flat, FlatAdmin)


class ComplaitAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", "appartment",)

admin.site.register(Complait, ComplaitAdmin)
