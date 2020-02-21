from django.contrib import admin

from .models import Church, PictureChurch, ArcticleChurch


@admin.register(PictureChurch)
class PictureChurchAdmin(admin.ModelAdmin):
    list_display = ('id', 'created', 'edited', 'church', 'picture')
    list_filter = ('created', 'edited', 'church')


class PictureChurchInline(admin.TabularInline):
    model = PictureChurch
    extra = 0


@admin.register(ArcticleChurch)
class ArcticleChurchAdmin(admin.ModelAdmin):
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


class ArcticleChurchInline(admin.TabularInline):
    model = ArcticleChurch
    extra = 0


@admin.register(Church)
class ChurchAdmin(admin.ModelAdmin):
    inlines = (PictureChurchInline, ArcticleChurchInline, )
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
