from django.contrib import admin

from .models import Author, ArticleAuthor


class ArticleChurchInline(admin.TabularInline):
    model = ArticleAuthor
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = (ArticleChurchInline,)
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'name',
        'birth_date',
        'race',
        'state',
        'city',
    )
    list_filter = ('created', 'edited', 'valid')
    search_fields = ('name',)


@admin.register(ArticleAuthor)
class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'author',
        'url',
    )
    list_filter = ('created', 'edited', 'valid', 'author')
