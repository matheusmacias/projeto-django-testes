from django.contrib import admin

from .models import *


admin.site.register(Category)
admin.site.register(Image)


class CategoryInline(admin.TabularInline):
    model = Post.categories.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    exclude = ('categories',)
    search_fields = ('title', 'body')
    inlines = [CategoryInline]
