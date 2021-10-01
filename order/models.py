from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import *
from stay.models import *
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class order(models.Model):
    user = models.OneToOneField(user, verbose_name=_("user"), on_delete=models.CASCADE, null=True, blank=True)
    fname = models.CharField(_("first name"), max_length=50, null=True, blank=True)
    mname = models.CharField(_("middle name"), max_length=50, null=True, blank=True)
    lname = models.CharField(_("last name"), max_length=50, null=True, blank=True)
    idnumber = models.IntegerField(_("id number"), null=True, blank=True)
    usphone = PhoneNumberField(_("phone number"), null=True, blank=True)
    usaddres = models.CharField(_("address"), max_length=50, null=True, blank=True)
    bdetail = models.ManyToManyField(stay, verbose_name=_("book detail"))
    totprc = models.IntegerField(_("total price"), null=True, blank=True)
    bookat = models.DateTimeField(_("booked at"), default= datetime.now)
    books = models.DateTimeField(_("start booking in"), auto_now=False, auto_now_add=False, blank=True, null=True)

    class Meta:
        ordering = ("bookat",)
    def __str__(self):
        return f"user name is : {self.fname} {self.mname} has an confirmation order by total price is {self.totprc}"