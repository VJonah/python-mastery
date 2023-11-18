# readrides.py

import collections
import csv
from collections import namedtuple, Counter


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

class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = [] # Columns
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
       # All lists assumed to have the same length
       return len(self.routes)

    def __getitem__(self, key):
        if isinstance(key,slice):
            r = RideData()
            # we unpack the tuple returned by the indices method
            for i in range(*key.indices(len(self))):
                r.append(self[i])
            return r
        return {
            'route': self.routes[key],
            'date': self.dates[key],
            'daytype': self.daytypes[key],
            'rides': self.numrides[key]
        }

    def append(self,d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


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

def read_rides_as_dicts(filename):
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

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    records = RideData()
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            record = {
                'route': row[0],
                'date': row[1],
                'daytype': row[2],
                'rides': int(row[3]),
            }
            records.append(record)
    return records


def count_routes(rows:list):
    '''
    Takes a list of row dictionaries and returns the number of bus routes.
    '''
    #if not isinstance(rows[0],dict):
        #raise TypeError(f"Function expects a list of dicts as argument. Got: {type(rows)}")
    return len({record['route'] for record in rows})

def number_of_passengers(rows:dict,route:str,date:str):
    '''
    Returns the number of passengers on a specific route on a specific date.
    '''
    #if not isinstance(rows[0],dict):
        #raise TypeError(f"Function expects a list of dicts as argument. Got: {type(rows)}")
    passengers = Counter()
    for record in rows:
        passengers[record['route'],record['date']] += record['rides']
    return passengers[route,date]

def total_rides(rows:dict):
    '''
    Returns the total number of passengers on a specific route.
    '''
    #if not isinstance(rows[0],dict):
        #raise TypeError(f"Function expects a list of dicts as argument. Got: {type(rows)}")
    rides = Counter()
    for record in rows:
        rides[record['route']] += record['rides']
    return rides

def greatest_increase(rows:dict,from_year='2001',to_year='2011'):
    '''
    Returns the 5 routes with the greatest increase between 2 years.
    '''
    #if not isinstance(rows[0],dict):
        #raise TypeError(f"Function expects a list of dicts as argument. Got: {type(rows)}")
    #elif not isinstance(from_year,str) or not isinstance(to_year,str):
        #raise TypeError(f"Function expects the from_year and to_year keyword arguments to be strings. Got: {type(from_year)} and {type(to_year)}")
    from_year_rides = Counter()
    to_year_rides = Counter()
    for record in rows:
        record_year = record['date'].split('/')[-1]
        if  record_year == from_year:
            from_year_rides[record['route']] += record['rides']
        elif record_year == to_year:
            to_year_rides[record['route']] += record['rides']
    rides_delta = to_year_rides - from_year_rides
    return rides_delta.most_common(5)





if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    #rows = read_rides_as_tuples('Data/ctabus.csv')
    #tuple_results = tracemalloc.get_traced_memory()
    #print('Tuple Memory Use: Current %d, Peak %d' % tuple_results)
    #tracemalloc.reset_peak()
    #rows = read_rides_as_dicts('Data/ctabus.csv')
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
    #rows = read_rides_as_class_with_slots('Data/ctabus.csv')
    #class_with_slots_results = tracemalloc.get_traced_memory()
    #print('Class with Slots Memory Use: Current %d, Peak %d' % class_with_slots_results)

# class with __slots__ takes it!
#rows = read_rides_as_dicts('Data/ctabus.csv')
