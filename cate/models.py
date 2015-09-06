from django.db import models


class Category(models.Model):
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

    def __unicode__(self):
        return self.cate_name

    def parent_counter(self):
        if self.category:
            pass


# Create your models here.
