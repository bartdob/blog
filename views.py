from django.shortcuts import render

posts = [
    {
        'author': 'BD',
        'title': 'Blog post',
        'content': 'First',
        'date': '11111'
    },
    {
        'author': 'Paulina',
        'title': 'Blog post2',
        'content': 'second',
        'date': '11111'
    }


]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

# Create your views here.