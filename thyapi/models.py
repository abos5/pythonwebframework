from thyapi import exceptions, forms


class KeyPrefix(object):
    '''A help class to be implemented by subclass with a key
    so we can use it to auto prefix key to reading from redis
    '''


class BaseModel(object):

    def __init__(self, data):
        '''initialize model.data
        '''
        if isinstance(data, forms.BaseForm):
            self.data = data.data
        elif isinstance(data, dict):
            self.data = data
        else:
            raise exceptions.InvalidDataType

    def validate(self):
        pass

    def save(self):
        self.validate()
        if self.hasError():
            return self.errors
        self.redClient().hmset(self.data)

    def hasError(self):
        return len(self.errors)

    @classmethod
    def redClient(cls):
        '''
        should be override and return a red connection
        '''


class Article(BaseModel):
    tags = None
    title = None
    category = None
    uniqid = None
    content = None
    create_datetime = None
    publish_datetime = None
    last_modified_datetime = None

    @staticmethod
    def redServers():
        return ('test.thyapi',)


class Category(object):
    pass


# eof
