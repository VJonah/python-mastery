# pcost.py


path = 'Data/portfolio.dat'

def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename,'r') as f:
        for row in f:
            _, shares, price = row.split()
            try:
                total_cost += int(shares) * float(price)
            # catches the failed int() and float() conversions above
            except ValueError as e:
                print(f"Couldn't parse: {repr(row)}")
                print(f"Reason: {e}")
    return total_cost


if __name__ == '__main__':
    print(portfolio_cost('Data/portfolio.dat'))
