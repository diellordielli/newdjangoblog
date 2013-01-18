from django.db import models
from django.contrib.auth.models import User
import datetime
from tagging.fields import TagField
from tagging.models import Tag
from django.db import models
from django.contrib.comments.models import Comment
from django.db.models import permalink


class Category(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 40, unique=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ("category_detail", (), {"categorySlug": self.slug})

class Post(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField()
    text = models.TextField()
    slug = models.SlugField(max_length = 40, unique=True)
    author = models.ForeignKey(User)
    categories = models.ManyToManyField(Category, blank = True, null = True, through = 'CategoryToPost')

    class Meta:
        ordering = ["-pub_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

class CategoryToPost(models.Model):
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)
