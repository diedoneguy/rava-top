from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField()

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

class WhyChoiceUs(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=200)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name ='why choise us'
        verbose_name_plural = 'why choice us'

class Chef(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    def __str__(self) -> str:
        return self.name
        