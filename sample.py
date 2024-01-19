# sample.py

from logcall import logged, logformat
from validate import Integer, validated, enforce

@logged
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y

@logged
@validated
def pow(x: Integer, y:Integer) -> Integer:
    return x ** y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def mul(x,y):
    return x*y


class Spam:
    @logformat('{func.__name__}')
    def instance_method(self):
        pass

    @classmethod
    @logformat('{func.__name__}')
    def class_method(cls):
        pass

    @logformat('{func.__name__}')
    @staticmethod
    def static_method():
        pass

    @property
    @logformat('{func.__name__}')
    def property_method(self):
        pass
