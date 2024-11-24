from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from = "name", unique = True , null=True, default=None)

    def save (self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            self.slug = f"{base_slug}"
        super().save(*args, **kwargs)
    def __str__(self) -> str:
        return self.name