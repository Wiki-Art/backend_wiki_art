from django.db import models
from utils.models_mixing import InformationMixing, TimesTempMixing
from utils.choices import UF_CHOICES
from django.utils.translation import ugettext_lazy as _
from author.models import Author
from church.models import Church


class WorkArt(InformationMixing, TimesTempMixing):
    name = models.CharField(_('name work of art'), max_length=100, unique=True)
    title = models.CharField(_('title work of art'),
                             max_length=100, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    state = models.CharField(_('state abbreviation'), max_length=2,
                             choices=UF_CHOICES)
    city = models.CharField(_('city'), max_length=100)

    def __str__(self):
        return self.name


class PictureWorkArt(TimesTempMixing):
    work_art = models.ForeignKey(
        WorkArt, on_delete=models.CASCADE, related_name='arts')
    picture = models.ImageField(_('picture image'))

    def __str__(self):
        return '{} - {}'.format(self.id, self.work_art.name)


class ArcticleWorkArt(InformationMixing, TimesTempMixing):
    work_art = models.ForeignKey(
        WorkArt, on_delete=models.CASCADE, related_name='articles')
    url = models.CharField(_('url article'), max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.id, self.work_art.name)
