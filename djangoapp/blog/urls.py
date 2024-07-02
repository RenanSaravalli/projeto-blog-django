from django.urls import path
from blog.views import index
app = 'blog'

urlpatterns = [
    path('', index, name='index'),
]
