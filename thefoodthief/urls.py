from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^posts/', include('posts.urls', namespace='posts')), 
    url(r'^admin/', admin.site.urls),
]

