"""
"""
from django.contrib import admin

from .models import City, TownType, Town, District


class CityAdmin(admin.ModelAdmin):
    # list_display = ["__all__", ]

    ordering = ['id', ]

class TownTypeAdmin(admin.ModelAdmin):
    # list_display = ["__all__", ]

    ordering = ['id', ]

class TownAdmin(admin.ModelAdmin):
    # list_display = ["__all__", ]

    ordering = ['id', ]

class DistrictAdmin(admin.ModelAdmin):
    # list_display = ["__all__", ]

    ordering = ['id', ]


admin.site.register(City, CityAdmin)
admin.site.register(TownType, TownTypeAdmin)
admin.site.register(Town, TownAdmin)
admin.site.register(District, DistrictAdmin)
