from django.contrib import admin

from .models import Category, Location, Post

admin.site.empty_value_display = 'Не задано'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'is_published', 'created_at')


class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_published', 'created_at')


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


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
