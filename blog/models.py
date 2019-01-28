from django.db import models
from django.utils.translation import ugettext_lazy as _


class Car(models.Model):
    """Car Model"""

    class Meta(object):
        verbose_name = _(u"Car")
        verbose_name_plural = _(u"Cars list")

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"First Name"))

    year = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Year"))

    price = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=_(u"Price"))

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)
