from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, CategoryForm
from .models import Post, Category




def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'posts/post_list.html', {'post_list': queryset})

def post_detail(request, year, month, day, post):
    post = Post.objects.get(slug            = post,
                            status          = 'published',
                            publish__year    = year,
                            publish__month   = month,
                            publish__day     = day)
    return render(request, 'posts/post_detail.html', {'post':post})

# - I would change line 124 to this: post = Post.objects.last(), just to make sure you can get any value
#[18:27] <mcspud> And then once that works, experiment with .get()

def post_create(request):
    return HttpResponse('post create')

def post_update(request):
    return HttpResponse('post update')

def post_delete(request):
    return HttpResponse('post delete')


