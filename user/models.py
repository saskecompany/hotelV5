from django.db import models
from django.forms.widgets import HiddenInput
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class user(models.Model):
    usip = models.CharField(_("user ip"), max_length=256, null=True, blank=True)
    usbookfav=models.ManyToManyField("home.roomM", verbose_name=_("favourit rooms"), related_name="favouritroom")
    usrobook=models.ManyToManyField("home.roomM", verbose_name=_("booked rooms"), related_name="bookroom")

    def __str__(self):
        return str(self.usip)