from django.contrib import admin

from .models import Apartments


class ApartmentsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "price", "is_publish",'is_favorite')
    list_display_links = ("id", "title", "price")
    list_editable = ("is_publish", 'is_favorite')
    search_fields = ("title", "price", "description")
    list_filter = ("city", "realtor", "square_all", "list_date", 'is_favorite')
    list_per_page = 30


admin.site.register(Apartments, ApartmentsAdmin)
