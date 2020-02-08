from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

posts = [
    {
        "author": "Sandeep",
        'title': "Blog Post1",
        'content': "First content",
        'date_posted': "Jan 1, 2020"
    },
    {
        "author": "Basva",
        'title': "Blog Post2",
        'content': "Second content",
        'date_posted': "Jan 10  , 2020"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, 'blog/home.html', context=context)


def about(request):
    return render(request, 'blog/about.html', context={"title": "Latest"})

