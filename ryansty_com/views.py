from django.shortcuts import render
from blog.models import Article, Tag

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    tag_list = Tag.objects.all()
    params = {
        'post_list': post_list,
        'tag_list': tag_list,
    }

    return render(request, 'home.html', params)

def test(request):
    return render(request, 'test.html')
