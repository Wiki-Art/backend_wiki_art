from django.db import models
from utils.models_mixing import InformationMixing, TimesTempMixing
from utils.choices import UF_CHOICES, RACE_CHOICE
from django.utils.translation import ugettext_lazy as _


class Author(InformationMixing, TimesTempMixing):
    name = models.CharField(_('name author'), max_length=100, unique=True)
    birth_date = models.DateField(blank=True, null=True)
    race = models.CharField(_('race of author'),
                            max_length=20, choices=RACE_CHOICE)
    state = models.CharField(_('state abbreviation'), max_length=2,
                             choices=UF_CHOICES)
    city = models.CharField(_('city'), max_length=100)

    def __str__(self):
        return '{} - {}'.format(self.id, self.name)


class ArticleAuthor(InformationMixing, TimesTempMixing):
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='articles')
    url = models.CharField(_('url article'), max_length=200)

    def __str__(self):
        return '{} - {}'.format(self.id, self.author.name)
