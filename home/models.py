from django.db import models
from django.db.models.fields import SlugField
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _
# Create your models here.
class serviceM(models.Model):
    slogo = models.ImageField(_("logo's service"), upload_to="services logos", null="true", blank="true")
    stitle = models.CharField(_("title's service"), max_length=10)
    sdes = models.TextField(_("description of service"))
    class Meta:
        db_table= "service"
        verbose_name= "service"
    def __str__(self):
        return self.stitle

class roomM(models.Model):
    def roimage(self, filename):
        file, ext = filename.split(".")
        return "room images/%s %s/%s.%s" %(self.roname, self.id , self.roname, ext)
    roimage1 = models.ImageField(_("rooms's image1"), upload_to=roimage, null="true", blank="true")
    roimage2 = models.ImageField(_("rooms's image2"), upload_to=roimage, null="true", blank="true")
    roimage3 = models.ImageField(_("rooms's image3"), upload_to=roimage, null="true", blank="true")
    roimage4 = models.ImageField(_("rooms's image4"), upload_to=roimage, null="true", blank="true")
    roimage5 = models.ImageField(_("rooms's image5"), upload_to=roimage, null="true", blank="true")
    roimage6 = models.ImageField(_("rooms's image6"), upload_to=roimage, null="true", blank="true")
    roimage7 = models.ImageField(_("rooms's image7"), upload_to=roimage, null="true", blank="true")
    roimage8 = models.ImageField(_("rooms's image8"), upload_to=roimage, null="true", blank="true")
    roimage9 = models.ImageField(_("rooms's image9"), upload_to=roimage, null="true", blank="true")
    roname = models.CharField(_("room's name"), max_length=10)
    rodes = models.TextField(_("room's description"))
    roprice = models.IntegerField(_("room's price"))
    roomoldprice = models.IntegerField(_("room's previous price"), null="true", blank="true")
    ronew= models.BooleanField(_("is new"), default=False)
    roavaliable= models.BooleanField(_("is avaliable"), default=True)
    ropostat = models.DateTimeField(_("published at"), auto_now=True)
    roslug = SlugField(max_length=10, null="true", blank="true")
    class Meta:
        db_table= "room"
        verbose_name= "room"
        ordering = ['-roavaliable', '-ropostat']

    def save(self, *args, **kwargs):
        if not self.roslug:
            self.roslug = slugify(self.roname)
        super(roomM ,self).save(*args, **kwargs)


    # def save(self, force_insert: bool, force_update: bool, using: Optional[str], update_fields: Optional[Iterable[str]]) -> None:


    def __str__(self):
        return f"{self.roname}"
