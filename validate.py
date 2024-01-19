# validate.py

import inspect
from functools import wraps

class ValidatedFunction:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        sig = inspect.signature(self.func)
        bound = sig.bind(*args,**kwargs)
        for name, value in bound.arguments.items():
            self.func.__annotations__[name].check(value)

        result = self.func(*args,**kwargs)

        if self.func.__annotations__['return']:
            self.func.__annotations__['return'].check(result)

        return result

def validated(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        sig = inspect.signature(func)
        bound = sig.bind(*args,**kwargs)
        annotations = dict(func.__annotations__)
        return_check = annotations.pop('return', None)
        exceptions = []
        for name, value in annotations.items():
            try:
                value.check(bound.arguments[name])
            except TypeError as e:
                exceptions.append(f'{name}: {e}')

        if exceptions:
            raise TypeError('Bad Arguments\n\t%s' % '\n\t'.join(exceptions))

        result = func(*args,**kwargs)

        if return_check:
            try:
                return_check.check(result)
            except TypeError as e:
                raise TypeError(f'Bad return: {e}')
        return result

    return wrapper

def enforce(**annotations):
    def validated(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            sig = inspect.signature(func)
            bound = sig.bind(*args,**kwargs)
            return_check = annotations.pop('return_', None)
            exceptions = []
            for name, value in annotations.items():
                try:
                    value.check(bound.arguments[name])
                except TypeError as e:
                    exceptions.append(f'{name}: {e}')

            if exceptions:
                raise TypeError('Bad Arguments\n\t%s' % '\n\t'.join(exceptions))

            result = func(*args,**kwargs)

            if return_check:
                try:
                    return_check.check(result)
                except TypeError as e:
                    raise TypeError(f'Bad return: {e}')

            return result
        return wrapper
    return validated



class Validator:

    def __init__(self, name=None):
        self.name = name


    def __set_name__(self, cls, name):
        self.name = name

    @classmethod
    def check(cls, value):
        return value

    def __set__(self, instance, value):
        instance.__dict__[self.name] = self.check(value)


class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError(f'Expected {cls.expected_type}')
        return super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        return super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        return super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    @property
    def cost(self):
        return self.shares * self.price

    @validated
    def sell(self, nshares:PositiveInteger):
        self.shares -= nshares
s = Stock('GOOG',23,32.4)