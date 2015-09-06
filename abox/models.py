from django.db import models


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

    class Meta:
        abstract = True



#eof
