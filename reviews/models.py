from django.db import models

# Create your models here.
class reM(models.Model):

    def img(self, filename):
        file, ext = filename.split(".")
        return "reimage/%s.%s" %(self.rename, ext)

    rename = models.CharField(verbose_name="your name", max_length=10)
    reimage = models.ImageField(verbose_name="your photo", upload_to=img)
    redes = models.TextField(verbose_name="your comment", )
    rerate = models.IntegerField(verbose_name="your rate", )

    class Meta:
        verbose_name="rate"
        ordering = ['-rerate']

    def __str__(self):
        return f"{self.rename}  {self.rerate} stars"