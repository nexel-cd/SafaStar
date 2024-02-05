from django.db import models
from django.utils.text import slugify

# Create your models here.


from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField 


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blogpost(models.Model):
    title = models.CharField(max_length=400)
    slug = models.SlugField(max_length=400, unique=True,blank=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    img1 = models.ImageField(("Banner Image 860 * 440"), upload_to="blog/Banner")
    content = RichTextField()
    img2 = models.ImageField((" Image 370 * 260"), upload_to="blog/post")
    img3 = models.ImageField((" Image 370 * 260"), upload_to="blog/post")
    quote = models.CharField(("Quote"), max_length=550)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)



    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
