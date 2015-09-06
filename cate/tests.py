

from django.test import TestCase
from cate.models import Category


class CategoryRelation(TestCase):
    fixtures = ['category']

    def test_relation(self):
        first = Category.objects.get(pk=2)
        self.assertEqual(first.cate_parent.cate_name == u'root', True)
        self.assertEqual(
            first.cate_children.all()[0].cate_name == u'the very second',
            True)


# eof
