from django.contrib import admin

from .models import Church, PictureChurch, ArticleChurch


@admin.register(PictureChurch)
class PictureChurchAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'edited', 'church', 'picture')
    list_filter = ('created', 'edited', 'church')


class PictureChurchInline(admin.TabularInline):
    model = PictureChurch
    extra = 0


@admin.register(ArticleChurch)
class ArticleChurchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'church',
        'url',
    )
    list_filter = ('created', 'edited', 'valid', 'church')


class ArticleChurchInline(admin.TabularInline):
    model = ArticleChurch
    extra = 0


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    inlines = (PictureChurchInline, ArticleChurchInline, )
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'name',
        'year_foundation',
        'state',
        'city',
    )
    list_filter = ('created', 'edited', 'valid')
    search_fields = ('name',)
