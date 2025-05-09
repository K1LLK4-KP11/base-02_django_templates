from django.shortcuts import render

# Create your views here.

# posts/views.py  
from django.shortcuts import render  
from .models import Post  

def post_list(request):  
    posts = Post.objects.all()  
    return render(request, 'posts/list.html', {'posts': posts})  