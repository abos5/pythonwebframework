from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=127, blank=False)
    create_datetime = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    last_modifed_datetime = models.DateTimeField(
        auto_now=True,
        null=True
    )
    publish_datetime = models.DateTimeField(
        null=True,
    )
    sort_datetime = models.DateTimeField(
        null=True,
    )

    class Meta:
        abstract = True

    @property
    def next_pk(self):
        return self.pk + 1

    @property
    def previous_pk(self):
        previous_pk = self.pk - 1
        return previous_pk if previous_pk > 0 else 1


class Category(models.Model):
    """
    General layout of category tables.
    It's better to set this class abstract.
    Avoid noise, increase query speed.
    """
    cate_id = models.AutoField(
        primary_key=True,
    )
    cate_name = models.CharField(max_length=63, blank=False)
    cate_description = models.CharField(max_length=127, null=True)
    cate_parent = models.ForeignKey(
        'self',
        null=True,
        db_constraint=False,
        default=1,
        related_name='cate_children'
    )

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.cate_name


class HtmlTextField(models.TextField):
    """
    declared to be used for formfield override
    """

    pass



#eof
