from django.shortcuts import render
from meals.models import Meals, Category
from blog.models import Post
from abouts.models import WhyChoiceUs


# Create your views here.

def home(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    posts = Post.objects.all()
    latest_post = Post.objects.last()
    why_choice_us = WhyChoiceUs.objects.all()

    context = {
        'meals': meals,
        'categories': categories,
        'posts': posts,
        'latest_post': latest_post,
        'why_choice_us': why_choice_us,
    }

    return render(request, 'index.html', context)
