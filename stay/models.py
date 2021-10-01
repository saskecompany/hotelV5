from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import user
from home.models import roomM
# Create your models here.
class stay(models.Model):
    ipuser = models.ForeignKey(user, verbose_name=_("user ip"), on_delete=models.CASCADE , unique=False)
    brom = models.OneToOneField(roomM, verbose_name=_("room"), on_delete=models.CASCADE, null=True , blank=True)
    stay = models.IntegerField(_("long stay"),null=True , blank=True)
    sroprice = models.BigIntegerField(_("rom price"), null=True , blank=True)
    srooldprice =models.BigIntegerField(_("previous rom price"), null=True , blank=True)
    totprice = models.BigIntegerField(_("total price"), null=True , blank=True)
    bookat = models.DateTimeField(_("booked at"), default= datetime.now)
    books = models.DateTimeField(_("start booking in"), auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        ordering = ("-bookat",)

    def __str__(self):
        return f"user has ip: {self.ipuser} booked the {self.brom} Room for{self.stay} day by final price is {self.totprice}$"