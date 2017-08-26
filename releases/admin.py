from django.contrib import admin

from .models import Release, Track, Link

# Register your models here.


class TrackInline(admin.TabularInline):
    model = Track
    extra = 2


class LinkInline(admin.TabularInline):
    model = Link
    extra = 2


class ReleaseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}
    inlines = [TrackInline, LinkInline]
    list_display = ('title', 'release_date')


admin.site.register(Release, ReleaseAdmin)
