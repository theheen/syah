from django.contrib import admin

from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'is_published', 'pub_datetime')
    ordering = ['-pub_datetime']


admin.site.register(Blog, BlogAdmin)
