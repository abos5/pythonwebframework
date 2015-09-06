

from django.test import TestCase
from cate.models import Category


class CategoryRelation(TestCase):

    def test_root_cate(self):
        root = Category()
        root.cate_name = "root"
        root.cate_description = "some description"
        root.cate_parent = root
        assert root.save()


# eof
