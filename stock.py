# stock.py


class Stock:
    __slots__ = ('name','_shares','_price')
    _types = (str, int, float) # a class variable

    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

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
        if not isinstance(value,self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        elif value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if not isinstance(value,self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        elif value < 0:
            raise ValueError("price must be >= 0")
        self._price = value


    def sell(self,nshares):
        '''Sells a certain number of shares.'''
        if nshares > self.shares:
            raise ValueError("Too few available shares to sell!")
        self.shares -= nshares

def print_portfolio(portfolio):
    '''
    Make a nicely formatted table showing stock data.
    '''
    print('%10s %10s %10s' % ('name','shares','price'))
    print(f"{'-' * 10} {'-' * 10} {'-' * 10}")
    #print(('-' * 10 + ' ') * 3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name,s.shares,s.price))
