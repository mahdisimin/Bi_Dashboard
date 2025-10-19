from django.db import models
from django.utils.text import slugify


# Create your models here.
class SavedQuery(models.Model) :
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    sql = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def SaveWithSlug(self , *args,**kwargs) :
        if not self.slug :
            base = slugify(self.title)
            condididate = base
            i = 1
            while SavedQuery.objects.filter(slug=condididate).exclude(pk=self.pk).exists() :
                condididate = f'{condididate}-{i}'
            self.slug = condididate

        super().save(*args, **kwargs)

    def __str__(self) :
        return f'{self.title} ({self.slug})'