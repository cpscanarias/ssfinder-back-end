from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class AACC(models.Model):

    class Meta:
        verbose_name = "Autonomous Community"
        verbose_name_plural = "Autonomous Comunities"

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=40)

    def __unicode__(self):
        return self.name


class Province(models.Model):

    class Meta:
        verbose_name = "Province"
        verbose_name_plural = "Provinces"

    code = models.CharField(max_length=5, unique=True)
    name = models.CharField(max_length=40)
    aacc = models.ForeignKey(AACC)

    def __unicode__(self):
        return self.name


class Town(models.Model):

    class Meta:
        verbose_name = "Town"
        verbose_name_plural = "Towns"

    name = models.CharField(max_length=40)
    province = models.ForeignKey(Province)

    def __unicode__(self):
        return self.name
