from django.contrib import admin

from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("title", "file", "is_active")
    list_filter = ("is_active",)
    list_editable = ("is_active",)
    search_fields = ("title",)
