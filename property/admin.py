from django.contrib import admin

from .models import Flat, Complait, Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',)
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year', 'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'floor', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
admin.site.register(Flat, FlatAdmin)


class ComplaitAdmin(admin.ModelAdmin):
    raw_id_fields = ('user', 'appartment',)

admin.site.register(Complait, ComplaitAdmin)


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('property',)
    list_display = ('owner',)

admin.site.register(Owner, OwnerAdmin)
