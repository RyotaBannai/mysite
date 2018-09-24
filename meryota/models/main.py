import datetime
from django.db import models
from django.utils import timezone

from django.conf import settings
from django.db.models.signals import post_save
def post_save_receiver(sender, instance, created, **kwargs):
    pass
post_save.connect(post_save_receiver, sender=settings.AUTH_USER_MODEL)

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    ###add for admin screen
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Category(models.Model):
    catname = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.catname

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    category =  models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
    @property
    def own_cat(self):
        return self.category
    class Meta:
        ordering = ["pub_date"]

from django.core import serializers
data = serializers.serialize("json", Question.objects.all())