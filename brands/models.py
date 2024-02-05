from django.db import models
from ckeditor.fields import RichTextField 
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class brandsitem(models.Model):
    brand= models.CharField(("Name"), max_length=50)
    img1 = models.ImageField(("Image 820 * 450"), upload_to='brands')
    des1 = RichTextField()
    quote = RichTextField()
    des2 = RichTextField()
    img2 = models.ImageField(("Image 545 * 505"), upload_to='brands')
    benefits = RichTextField()
    slug = models.SlugField(unique=True, max_length=150, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.brand)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.brand
    


class brandcontact(models.Model):
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    phono = models.CharField(("Phone Number"), max_length=250)
    brand = models.ForeignKey("brandsitem", verbose_name=("Product/Brand name"), on_delete=models.CASCADE)
    msg = RichTextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    

class brandfaq(models.Model):
    brand = models.ForeignKey("brandsitem", verbose_name=("Brand"), on_delete=models.CASCADE)
    question = models.TextField(("Question"))
    answer = models.TextField(("Answer"))  

    def __str__(self):
        return f'{self.brand} {self.question}'