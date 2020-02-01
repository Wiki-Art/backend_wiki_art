from django.db import models


class InformationMixin(models.Model):
    created = models.DateTimeField(editable=False, blank=True, auto_now_add=True)
    author_send = models.CharField(blank=False, null=False, max_length=50)
    valid = models.BooleanField(blank=False, null=False, default=False)
    
    class Meta:
        abstract = True