from email.policy import default
from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from fl_tags.models import Tags
from django.contrib.contenttypes.models import ContentType




class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    tags = GenericRelation(Tags)
    
class Choice(models.Model):
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
