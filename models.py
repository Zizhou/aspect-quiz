from django.db import models

# Create your models here.

class Aspect(models.Model):
    aspect = models.CharField(max_length = 200)
    
    def __unicode__(self):
	return self.aspect

class Word(models.Model):
    word = models.CharField(max_length = 200)
    aspect = models.ForeignKey(Aspect)
    
    def __unicode__(self):
	return self.word

class Question(models.Model):
    question = models.CharField(max_length = 1000)
    prime = models.CharField(max_length = 1000)
    order = models.IntegerField(default = 0)
    
    def __unicode__(self):
	return self.question
