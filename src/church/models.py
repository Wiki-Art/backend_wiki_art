from django.db import models
from utils.models_mixing import InformationMixing, TimesTempMixing
from utils.choices import UF_CHOICES
from django.utils.translation import ugettext_lazy as _


class Church(InformationMixing, TimesTempMixing):
    name = models.CharField(_('name church'), max_length=100, unique=True)
    year_foundation = models.PositiveIntegerField(_('year foundation'))
    state = models.CharField(_('state abbreviation'), max_length=2,
                             choices=UF_CHOICES)
    city = models.CharField(_('city'), max_length=100)

    def __str__(self):
        return self.name


class PictureChurch(TimesTempMixing):
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, related_name='pictures')
    picture = models.ImageField(_('picture image'))

    def __str__(self):
        return '{} - {}'.format(self.id, self.church.name)


class ArcticleChurch(InformationMixing, TimesTempMixing):
    church = models.ForeignKey(
        Church, on_delete=models.CASCADE, related_name='articles')
    url = models.CharField(_('url article'), max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.id, self.church.name)
