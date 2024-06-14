
from django.shortcuts import render
from categories_app.models import Category
from post_app.models import Post

def home(request, category_slug = None):
    data = Post.objects.all()  
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)  
        data = Post.objects.filter(category = category)  
    categories = Category.objects.all()    
    return render(request, 'home.html', {'data' : data, 'category' : categories})   