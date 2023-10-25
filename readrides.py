# readrides.py

import csv
from collections import namedtuple


class RideRecord:
    def __init__(self,route,date,daytype,rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
class RideRecordS: # the __slots__ version
    __slots__ = ['route','date','daytype','rides']
    def __init__(self,route,date,daytype,rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides
#
# the named tuple version
RideRecordNT = namedtuple('RideRecordT',['route','date','daytype','rides'])

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as a list of dictionaries
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            }
            records.append(record)
    return records


def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of Row objects
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = RideRecord(row[0],row[1],row[2],int(row[3]))
            records.append(record)
    return records

def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of named tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = RideRecordNT(row[0],row[1],row[2],int(row[3]))
            records.append(record)
    return records

def read_rides_as_class_with_slots(filename):
    '''
    Read the bus ride data as a list of Row objects with __slots___
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows) # skip headers
        for row in rows:
            record = RideRecordS(row[0],row[1],row[2],int(row[3]))
            records.append(record)
    return records
if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('Data/ctabus.csv')
    #tuple_results = tracemalloc.get_traced_memory()
    #print('Tuple Memory Use: Current %d, Peak %d' % tuple_results)
    #tracemalloc.reset_peak()
    #rows = read_rides_as_dictionary('Data/ctabus.csv')
    #dictionary_results = tracemalloc.get_traced_memory()
    #print('Dictionary Memory Use: Current %d, Peak %d' % dictionary_results)
    #tracemalloc.reset_peak()
    #rows = read_rides_as_class('Data/ctabus.csv')
    #class_results = tracemalloc.get_traced_memory()
    #print('Class Memory Use: Current %d, Peak %d' % class_results)
    #tracemalloc.reset_peak()
    #rows = read_rides_as_named_tuple('Data/ctabus.csv')
    #named_tuple_results = tracemalloc.get_traced_memory()
    #print('Named Tuple Memory Use: Current %d, Peak %d' % named_tuple_results)
    #tracemalloc.reset_peak()
    rows = read_rides_as_class_with_slots('Data/ctabus.csv')
    class_with_slots_results = tracemalloc.get_traced_memory()
    print('Class with Slots Memory Use: Current %d, Peak %d' % class_with_slots_results)

# class with __slots__ takes it!
