from django.db import models
from ckeditor.fields import RichTextField 
from django.utils.text import slugify
from django.utils import timezone
# Create your models here.


class products(models.Model):
    name = models.CharField(("Name"), max_length=50)
    des = RichTextField()
    img = models.ImageField(("Image 2580 * 1200"), upload_to='product')

    slug = models.SlugField(unique=True, max_length=150, blank=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class productitem(models.Model):
    product = models.ForeignKey("products", verbose_name=("Product"), on_delete=models.CASCADE)
    brand = models.ForeignKey("brands.brandsitem", verbose_name=("Brand"), on_delete=models.CASCADE)
    img = models.ImageField(("Image"), upload_to="product/item")


    
class productcontact(models.Model):
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    phono = models.CharField(("Phone Number"), max_length=250)
    product = models.ForeignKey("products", verbose_name=("Product/Brand name"), on_delete=models.CASCADE)
    msg = RichTextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
    
