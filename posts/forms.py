from django import forms
from .models import Post, Category

class PostForm(forms.ModelForm):
    class Meta:
        model   = Post
        fields  = [
                'title',
                'body',
                'publish',
                'status',
                'categories',
            
                ]

class CategoryForm(forms.ModelForm):
    class Meta:
        model   = Category
        fields  = [
                'category_name',
                'category_slug',
                ]


    
    