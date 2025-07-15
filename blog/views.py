from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from random import randint

from blog.forms import BlogForms
from blog.models import Blog

@login_required
def home(request):
    blogs = Blog.objects.filter(published_at=True)
    search_published_blog = request.GET.get('search_published_blog')
    if search_published_blog:
        blogs = Blog.objects.filter(
            Q(title__icontains=search_published_blog) | Q(content__icontains=search_published_blog),published_at=True)
    context={
        "blogs":blogs
    }
    return render(request,'blog/home.html',context=context)


def create(request):
    if request.method == "POST":
        form = BlogForms(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
         form = BlogForms()
    context = {
        "form":form
    }
    return render(request,'blog/create.html',context=context)


def detail(request,blog_id):
    blog=get_object_or_404(Blog , id=blog_id)
    context={
        'blog':blog
    }
    return render(request,'blog/detail.html',context=context)

def update(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == "POST":
        form = BlogForms(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForms(instance=blog)
    return render(request,'blog/update.html',{'form':form, 'blog':blog})

def delete(request,blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    return redirect('home')