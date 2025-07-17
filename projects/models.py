from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    year =  models.IntegerField()
    image = models.ImageField(upload_to='projects/')
    link = models.URLField(blank=True)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return f'{self.title} - {self.year}'