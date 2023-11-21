# stock.py


class Stock:
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price

    def cost(self):
        '''Returns the cost of the stock.'''
        return self.shares * self.price

    def sell(self,nshares):
        '''Sells a certain number of shares.'''
        if nshares > self.shares:
            raise ValueError("Too few available shares to sell!")
        self.shares -= nshares

def read_portfolio(file_path):
    '''
    Reads a CSV file of stock data into a list of Stocks.
    '''
    import csv
    stocks = []
    with open(file_path) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            name, shares, price = row
            s = Stock(name,int(shares),float(price))
            stocks.append(s)
    return stocks

def print_portfolio(portfolio):
    '''
    Make a nicely formatted table showing stock data.
    '''
    print('%10s %10s %10s' % ('name','shares','price'))
    print(f"{'-' * 10} {'-' * 10} {'-' * 10}")
    #print(('-' * 10 + ' ') * 3)
    for s in portfolio:
        print('%10s %10d %10.2f' % (s.name,s.shares,s.price))
