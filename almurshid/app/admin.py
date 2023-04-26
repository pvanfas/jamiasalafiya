from django.contrib import admin

from .models import About, Book, Message, News, Social, Wish


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "content", "is_active")


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "subtitle", "is_active")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "message", "is_active")


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "is_active")


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    pass


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ("media", "link", "is_active")


admin.site.site_header = "Al-Murshid Administration"
admin.site.site_title = "Al-Murshid Admin Portal"
admin.site.index_title = "Welcome to Al-Murshid Admin Portal"
