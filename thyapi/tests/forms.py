from tornado.testing import AsyncTestCase, gen_test
from thyapi import forms, models, exceptions, settings
from . import fixtures


class BaseFormTestCase(AsyncTestCase):

    def test_validate(self):
        '''BaseForm.validate should be override by it's sub classes
        '''
        form = forms.BaseForm(dict())
        self.assertRaises(exceptions.UnimplementedError, form.validate)


class SublimeArticleFormTestCase(AsyncTestCase):

    def test_validate(self):
        article = fixtures.sublimeArticles['article_0']
        self.assertEquals(
            forms.BaseForm(article).validate(),
            settings.ValidateCode.success
        )

    def test_data_submit(self):
        pass














#eof
