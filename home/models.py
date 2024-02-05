from django.db import models
from ckeditor.fields import RichTextField 
# Create your models here.
class contact(models.Model):
    name = models.CharField(("Name"), max_length=250)
    email = models.CharField(("Email"), max_length=250)
    phono = models.CharField(("Phone Number"), max_length=250)
    msg = RichTextField()

    def __str__(self):
        return self.name
    
