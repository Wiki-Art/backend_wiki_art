from django.db import models


class TimesTempMixing(models.Model):
    created = models.DateTimeField(
        editable=False, auto_now_add=True)
    edited = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class InformationMixing(models.Model):
    author_send = models.CharField(blank=False, null=False, max_length=100)
    valid = models.BooleanField(blank=False, null=False, default=False)

    class Meta:
        abstract = True
