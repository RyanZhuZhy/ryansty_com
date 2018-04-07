from django.shortcuts import render
from blog.models import Article

# Create your views here.
def page(request, id):
    post = Article.objects.get(id=id)
    return render(request, 'blog/page.html', {'post': post})

def pagelist(request):
    post_list = Article.objects.all()
    return render(request, 'blog/list.html', {'post_list': post_list})
