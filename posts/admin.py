from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = (
                    'title',
                    'slug',
                    'publish',
                    'status',         
            )

admin.site.register(Category)
admin.site.register(Post, PostAdmin)

