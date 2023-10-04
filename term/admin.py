from django.contrib import admin

from .models import Tag, Term


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_list')
    search_fields = ('name',)
    search_help_text = 'Search in names'
    list_filter = ('tags',)

    def tag_list(self, obj):
        return ', '.join(obj.tags.values_list('name', flat=True))
