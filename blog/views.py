from django.shortcuts import render
from blog.models import Article

# Create your views here.
def page(request, id):
    post = Article.objects.get(id=id)
    return render(request, 'blog/page.html', {'post': post})
