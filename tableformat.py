# tableformat.py


def print_table(objects,attr_names):
    '''
    Make a nicely formatted table showing object attributes.
    '''
    print('%10s '*len(attr_names) % tuple(attr_names))
    print(('-'*10 + ' ') * len(attr_names))
    for o in objects:
        print('%10s '*len(attr_names) % tuple([str(getattr(o,name)) for name in attr_names]))
