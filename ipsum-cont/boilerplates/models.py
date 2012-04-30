from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BoilerPlate(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add = True)
    date_modified = models.DateTimeField(null = True,blank = True)
    user = models.ForeignKey(User, related_name = "boilerplates")

#class FilePrint(models.Model):
#	thefile = models.FileField(upl)


#class ImageLoader(BoilerPlate.icon)