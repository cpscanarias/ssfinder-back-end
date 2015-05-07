from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

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


class SocialService(models.Model):

    class Meta:
        verbose_name = "Social Service"
        verbose_name_plural = "Social Services"

    name = models.CharField(max_length=40)
    categories = models.ManyToManyField(
        Category
    )
    address = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    town = models.ForeignKey(Town)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    description = models.TextField(
        'Description', 
        max_length=400, 
        blank=True,
        help_text="Optional"
    )
    web = models.CharField(max_length=50, blank=True)
    facebook = models.CharField(max_length=50, blank=True)
    twitter = models.CharField(max_length=30, blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    google_plus = models.CharField(max_length=50, blank=True)
    tumblr = models.CharField(max_length=50, blank=True)
