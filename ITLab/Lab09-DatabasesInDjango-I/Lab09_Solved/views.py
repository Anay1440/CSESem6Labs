from django.shortcuts import render, redirect
import datetime
from Lab09_Solved.models import BlogPost, BlogPostForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def archive(request):
    posts = BlogPost.objects.all()[:10]
    return render(request,'solved_archive.html', {'posts': posts, 'form': BlogPostForm()})

def create_blogpost(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.datetime.now()
            post.save()

        return redirect('/Solved/blog')
