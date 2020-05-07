# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import WorkArt, PictureWorkArt, ArticleWorkArt


class PictureWorkArtInline(admin.TabularInline):
    model = PictureWorkArt
    extra = 0


@admin.register(PictureWorkArt)
class PictureWorkArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'edited', 'work_art', 'picture')
    list_filter = ('created', 'edited', 'work_art')


class ArticleWorkArtInline(admin.TabularInline):
    model = ArticleWorkArt
    extra = 0


@admin.register(ArticleWorkArt)
class ArticleWorkArtAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'work_art',
        'url',
    )
    list_filter = ('created', 'edited', 'valid', 'work_art')


@admin.register(WorkArt)
class WorkArtAdmin(admin.ModelAdmin):
    inlines = (PictureWorkArtInline, ArticleWorkArtInline,)
    list_display = (
        'id',
        'created',
        'edited',
        'author_send',
        'valid',
        'name',
        'title',
        'author',
        'church',
        'state',
        'city',
    )
    list_filter = ('created', 'edited', 'valid', 'author', 'church')
    search_fields = ('name',)
