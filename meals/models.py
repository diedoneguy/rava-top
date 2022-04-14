from distutils.command.upload import upload
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.forms import CharField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    
    def __str__(self) -> str:
        return self.name

class Meals(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    people = models.IntegerField()
    is_specionality = models.BooleanField(blank=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=9)
    image = models.ImageField(upload_to = 'meals/%Y/%m/%d/')
    preparation_time = models.IntegerField()
    slug = models.SlugField(blank=True,null=True)

    def save(self, *args,**kwargs):
        self.slug =self.name
        return super(Meals , self). save( *args,**kwargs)

    class Meta:
        verbose_name = 'Meal'
        verbose_name_plural = 'Meals'

        def __str__(self) -> str:
            pass