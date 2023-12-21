# validate.py

class Validator:
    @classmethod
    def check(cls, value):
        return value

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
    __slots__ = ('name','_shares','_price')
    _types = (str, int, float) # a class variable

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"Stock({repr(self.name)}, {self.shares}, {self.price})"

    def __eq__(self, other):
        return isinstance(other, Stock) and ((self.name, self.shares, self.price) ==
                                           (other.name, other.shares, other.price))
    @classmethod
    def from_row(cls,row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)

    @property
    def cost(self):
        '''Returns the cost of the stock.'''
        return self.shares * self.price

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self,value):
        self._shares =  PositiveInteger.check(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        self._price = PositiveFloat.check(value)


    def sell(self,nshares):
        '''Sells a certain number of shares.'''
        if nshares > self.shares:
            raise ValueError("Too few available shares to sell!")
        self.shares -= nshares
