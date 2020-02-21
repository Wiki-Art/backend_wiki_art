from django.contrib import admin

from .models import Author, ArcticleAuthor


class ArcticleChurchInline(admin.TabularInline):
    model = ArcticleAuthor
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    inlines = (ArcticleChurchInline,)
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


@admin.register(ArcticleAuthor)
class ArcticleAuthorAdmin(admin.ModelAdmin):
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
