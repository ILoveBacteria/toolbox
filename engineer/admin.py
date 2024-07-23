from django.contrib import admin
from tomark import Tomark

from engineer.models import Tag, Term, Footprint, LeetcodeTopic, Leetcode, Vocabulary
from engineer.tasks import send_email_task


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_term')

    @admin.display(description='Number of terms')
    def count_term(self, obj):
        return obj.term_set.count() + obj.footprint_set.count()


@admin.register(LeetcodeTopic)
class LeetcodeTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'count_problem')

    @admin.display(description='Number of problems')
    def count_problem(self, obj):
        return obj.leetcode_set.count()


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag_list')
    search_fields = ('name',)
    search_help_text = 'Search in names'
    list_filter = ('tags',)
    actions = ('markdown', 'send_mail')

    def tag_list(self, obj):
        return ', '.join(obj.tags.values_list('name', flat=True))

    @admin.action
    def markdown(self, request, queryset):
        table = Tomark.table(queryset.values())
        with open('markdown.md', 'w') as f:
            f.write(table)

    @admin.action
    def send_mail(self, request, queryset):
        message = ', '.join(queryset.values_list('name', flat=True))
        send_email_task.delay(subject='Review selected terms form admin panel', message=message)


@admin.register(Footprint)
class FootprintAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'tag_list')
    search_fields = ('title',)
    list_filter = ('tags',)

    def tag_list(self, obj):
        return ', '.join(obj.tags.values_list('name', flat=True))


@admin.register(Leetcode)
class LeetcodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'problem_beauty', 'created_at', 'topic_list')
    search_fields = ('name',)
    list_filter = ('topics',)

    def topic_list(self, obj):
        return ', '.join(obj.topics.values_list('name', flat=True))
    

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = ('word', 'seen', 'know', 'know_rate')
    search_fields = ('name',)
    actions = ('know', 'dont_know')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = [
        (
            None,
            {
                'fields': ('word', 'seen', 'know', 'example'),
            },
        ),
        (
            'Translate',
            {
                'classes': ('collapse',),
                'fields': ('translation',),
            },
        ),
        (
            'Data & Time',
            {
                'fields': ('created_at', 'updated_at'),
            },
        ),
    ]

    @admin.action
    def know(self, request, queryset):
        for obj in queryset:
            obj.seen += 1
            obj.know += 1
            obj.save()
    
    @admin.action
    def dont_know(self, request, queryset):
        for obj in queryset:
            obj.seen += 1
            obj.save()
