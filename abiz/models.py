from django.db import models
import abox.models
from django.conf import settings


def content_file_name(instance, filename):
    return '/'.join([settings.UPLOAD_ROOT, filename])


class Article(abox.models.Post):
    article_id = models.AutoField(
        primary_key=True
    )
    summary = models.CharField(max_length=1023, blank=True)

    def __unicode__(self):
        return "%+32s" % (self.title)


class ArticleBody(models.Model):
    article = models.OneToOneField(
        Article,
        primary_key=True,
        db_constraint=False,
    )
    content = abox.models.HtmlTextField(blank=True, default='')


class ArticleCategory(abox.models.Category):
    """
    an specific category table for article only
    table structure inherits from category(abstract model of category)

    If no many to many fields using through as pivot table set
    then should reach articles and categories in these way:
    In [1]: ac = ArticleCategory.objects.get(pk=int)
    In [2]: ac.catedarticle_set.first().article
    Out[2]: <Article: git: git server : set up (version:Abos edited )>

    In [3]: ac.catedarticle_set.first().category
    Out[3]: <ArticleCategory: the very second>
    or declare this in class ArticleCategory
    In [4]: articles = models.ManyToManyField(
        ...     Article,
        ...     through='CatedArticle'
        ... )
    """


class CatedArticle(models.Model):
    """
    Where the relationship between article and article_category is stored.
    And the Article it self don't have to know.
    """
    category = models.ForeignKey(
        ArticleCategory,
        db_constraint=False,
    )
    article = models.ForeignKey(
        Article,
        db_constraint=False,
    )

    def __str__(self):
        return '%s: %s' % (self.category, self.article,)


class Image(models.Model):
    src = models.ImageField(upload_to=content_file_name)

    def __str__(self):
        return "%s/%s" % (settings.STATIC_DOMAIN, self.src)


class ImageOfArticle(models.Model):
    article = models.ForeignKey(
        Article,
        db_constraint=False,
    )

    image = models.ForeignKey(
        Image,
        db_constraint=False,
    )

    def __str__(self):
        return "image of article: %s" % self.article.pk()


# Create your models here.
