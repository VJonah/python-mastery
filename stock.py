# stock.py


class Stock:
    types = (str, int, float) # a class variable
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    @classmethod
    def from_row(cls,row):
        values = [func(val) for func, val in zip(cls.types, row)]
        return cls(*values)

    def cost(self):
        '''Returns the cost of the stock.'''
        return self.shares * self.price

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
