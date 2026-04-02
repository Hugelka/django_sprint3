from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published', 'created_at')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'created_at')


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'pub_date',
        'is_published',
        'created_at',
        'location',
        'category'
    )
