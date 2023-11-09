from django.contrib import admin
from tomark import Tomark

from .models import Tag, Term


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_term')

    @admin.display(description='Number of terms')
    def count_term(self, obj):
        return obj.term_set.count()


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_list')
    search_fields = ('name',)
    search_help_text = 'Search in names'
    list_filter = ('tags',)
    actions = ('markdown',)

    def tag_list(self, obj):
        return ', '.join(obj.tags.values_list('name', flat=True))

    @admin.action
    def markdown(self, request, queryset):
        table = Tomark.table(queryset.values())
        with open('markdown.md', 'w') as f:
            f.write(table)
