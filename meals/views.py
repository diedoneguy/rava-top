from multiprocessing import context
from unicodedata import category
from django.shortcuts import render
from .models import Category,Meals

def meal_list(request):
    meal_list = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        'meal_list':meal_list,
        'categories':categories
    }
    return render(request,'',context)

def meal_detail(request,slug):
    meal_detail = Meals.objects.get(slug=slug)
    context = {
        'meal_derail': meal_detail,

    }
    return render(request,'detail.html',context)