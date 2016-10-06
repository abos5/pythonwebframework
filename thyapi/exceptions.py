

class ThyapiError(Exception):

    def __str__(self):
        return self.code


class UnimplementedError(ThyapiError):
    code = 1



# eof
