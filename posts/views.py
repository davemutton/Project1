from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import PostForm, CategoryForm
from .models import Post, Category
from django.http import HttpResponseRedirect

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

def post_create(request):
    category_form = CategoryForm(request.POST or None)
    post_form = PostForm(request.POST or None)
    if category_form.is_valid(): 
        category_form_instance = category_form.save(commit=False)
      
    # if post_form.is_valid():         
    #     post_form_instance = post_form.save()
        
    context = {'post_form':post_form, 'category_form':category_form}
    return render(request, 'posts/post_form.html', context)

def post_update(request):
    return HttpResponse('post update')

def post_delete(request):
    return HttpResponse('post delete')
    
