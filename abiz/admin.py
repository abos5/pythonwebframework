from django.contrib import admin
from abiz.models import Article, CatedArticle
from abiz.models import ArticleBody, ArticleCategory, ImageOfArticle, Image
import abox.admin


class ArticleCategoryInline(abox.admin.AboxTabularInline):
    model = CatedArticle
    extra = 1
    max_num = 2

    def get_field_queryset(self, db, db_field, request):
        if db_field.name == 'category':
            return ArticleCategory.objects.filter()

        return super(ArticleCategoryInline, self).get_field_queryset(
            db, db_field, request)


class ArticleBodyInline(abox.admin.AboxTabularInline):
    model = ArticleBody
    extra = 1
    min_num = 1


class ImageOfArticleInline(abox.admin.AboxTabularInline):
    model = ImageOfArticle
    extra = 1
    max_num = 1


@admin.register(Article)
class ArticleAdmin(abox.admin.AboxModelAdmin):
    fieldsets = (
        (
            None, {
                'fields': (
                    'title', 'summary',
                ),
            },
        ),
        (
            None, {
                'fields': (
                    ['publish_datetime', 'sort_datetime', ],  # one line
                ),
            }
        ),
    )
    inlines = [
        ArticleCategoryInline,
        ArticleBodyInline,
        ImageOfArticleInline,
    ]


@admin.register(Image)
class ImageAdmin(abox.admin.AboxModelAdmin):
    pass

# Register your models here.
