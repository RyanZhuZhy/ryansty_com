from django.shortcuts import render
from blog.models import Article, Tag

# Create your views here.
def page(request, id):
    post = Article.objects.get(id=id)
    tag_list = Tag.objects.all()
    params = {
        'post': post,
        'tag_list': tag_list,
    }
    return render(request, 'blog/page.html', params)

def pagelist(request):
    post_list = Article.objects.all()
    tag_list = Tag.objects.all()
    params = {
        'post_list': post_list,
        'tag_list': tag_list,
    }
    return render(request, 'blog/list.html', params)
