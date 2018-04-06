from django.contrib import admin
from django.db import models
from pagedown.widgets import AdminPagedownWidget
from blog.models import Article
from blog.models import Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }

    list_display = ('title', 'pub_time')
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)
