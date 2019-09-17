from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tinymce import HTMLField
from django.urls import reverse

class Catagory(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField(
        default="This is overviewfield plsese add your minimum overview")
    content = HTMLField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    comment_count = models.IntegerField(default=0)
    thumbnail = models.ImageField(
        null=True, blank=True, upload_to='thumbnail_pics')
    catagories = models.ManyToManyField(Catagory, blank=True)

    def get_absolute_url(self):
        return reverse("blog-detail", kwargs={"pk": self.pk})
    

    def __str__(self):
        return f'Blog : {self.title}'
