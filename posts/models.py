from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse


class Category(models.Model):
    category_name       = models.CharField(max_length=250, unique=True)
    category_slug       = models.SlugField(max_length=250, unique=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    STATUS_CHOICES      = (
                            ('draft', 'Draft'),
                            ('published', 'Published'),
                            )

    title               = models.CharField(max_length=250)
    slug                = models.SlugField(max_length=250, 
                                            unique_for_date='publish')
    body                = models.TextField()
    publish             = models.DateTimeField(default=timezone.now)
    created             = models.DateTimeField(auto_now_add=True)
    updated             = models.DateTimeField(auto_now=True)
    status              = models.CharField(max_length=10, 
                                            choices=STATUS_CHOICES,
                                            default='draft')
    categories          = models.ManyToManyField(Category)

    def get_absolute_url(self):
        return reverse('posts:post_detail',
                args=[self.publish.year,
                    self.publish.strftime('%m'),
                    self.publish.strftime('%d'),
                    self.slug])

    def __str__(self):
        return self.title

    
    
    
