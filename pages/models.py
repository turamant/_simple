from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.
class Rubric(models.Model):
    name = models.CharField(max_length=100,unique=True)
    url = models.SlugField(max_length=100,unique=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('rubric_detail',kwargs={"slug": self.url})

class Post(models.Model):
    title = models.CharField(max_length=100,unique=True)
    rubric = models.ForeignKey(Rubric,on_delete=models.CharField,null=True,related_name="rubrics")
    foto_post = models.ImageField(upload_to='foto_post/',null=True)
    images = models.ManyToManyField("Image",related_name="post_image")
    url = models.SlugField(max_length=100,unique=True)
    body = models.TextField()
    post_data = models.DateField(auto_now_add=True,null=True)
    post_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.url})

class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/',null=True,blank=True)
    url = models.SlugField(max_length=100,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('image_detail',kwargs={"slug": self.url})

