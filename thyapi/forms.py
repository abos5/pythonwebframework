from exceptions import UnimplementedError


class BaseForm(object):
    '''form base class
    '''

    def __init__(self, data):
        self.data = data

    def validate(self):
        raise UnimplementedError


class SublimeArticle(BaseForm):
    '''validating articles uploaded from sublime text
    '''

    def validate(self):
        pass






# eof
