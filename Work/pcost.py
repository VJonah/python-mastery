# pcost.py


path = '../Data/portfolio.dat'
total_cost = 0

with open(path,'r') as f:
    for row in f:
        _, shares, price = row.split(' ')
        total_cost += int(shares) * float(price)
print(total_cost)
