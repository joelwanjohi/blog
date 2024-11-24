from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render , get_object_or_404, redirect

from HOME.models import Blog, Category

# Create your views here.
def index(request):
     post = Blog.objects.order_by('-id')
     main_post = Blog.objects.order_by('-id').filter(Main_post = True)[0:1]
     recent = Blog.objects.filter(section = 'Recent').order_by('-id')[:5]
     popular = Blog.objects.filter(section='Popular').order_by('-id')[0:5]
     cat = Category.objects.all()

     context = {
        'post': post,
        'main_post': main_post,
        'recent': recent, 
        'cat' : cat,
        'popular': popular

    }
     return render(request, "index.html")




def blog_detail(request,slug):
    # posts= Blog.objects.order_by('-id')
    category = Category.objects.all()
    post = get_object_or_404(Blog, blog_slug = slug)
#   increment view count
    post.views +=1
    post.save()

    # comments = Comment.objects.filter(blog_id = post.id).order_by('-date')

    context = {
        # 'posts': post,
         'category': category,
         'post' : post,
        #  'comments': comments
 
    }

    return render (request, "blog_detail.html", context)

def category(request, slug):
    cat = category.objects.all()
    blog_cat = category.objects.filter(slug=slug)
    context = {
        'cat': cat,
        'active_category' : slug,
        "blog_cat" : blog_cat,

    }
    return render (request, 'category.html',context)