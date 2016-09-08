from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm, CategoryForm
from .models import Post, Category


def post_list(request):
    queryset = Post.objects.all()
    return render(request, 'posts/post_list.html', {'post_list': queryset})

def post_detail(request, year, month, day, post):
    instance = get_object_or_404(Post, slug            = post,
                                       status          = 'published',
                                       publish__year   = year,
                                       publish__month  = month,
                                       publish__day    = day)
    return render(request, 'posts/post_detail.html', {'post':instance})

# - I would change line 124 to this: post = Post.objects.last(), just to make sure you can get any value
#[18:27] <mcspud> And then once that works, experiment with .get()

def post_create(request):
    post_form = PostForm(request.POST or None)
    category_form = CategoryForm(request.POST or None)
    if post_form.is_valid() and post_form.is_valid():
        instance = post_form.save(commit=False)
        instance.save()

    category_form = CategoryForm(request.POST or None)
    if category_from.is_valid():
        instance = category_form.save(commit=False)
        instance.save()

    context = {'post_form':post_form, 'category_form':category_form}
    return render(request, 'posts/post_form.html', context)

def post_update(request):
    return HttpResponse('post update')

def post_delete(request):
    return HttpResponse('post delete')


