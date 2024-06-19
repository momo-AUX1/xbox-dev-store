from django.db import models
from djrichtextfield.models import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=200)
    hidden = models.BooleanField(default=False) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    url = models.CharField(max_length=999, blank=True)
    file = models.FileField(upload_to='uploads/binaries')
    image = models.ImageField(upload_to='uploads/images')
    hidden = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label = 'XBOX'

    def __str__(self):
        return self.name
