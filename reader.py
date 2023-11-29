# reader.py

import csv
from abc import ABC, abstractmethod


class DataCollection:
    def __init__(self,headers):
        if len(headers) == 0:
            raise ValueError("DataCollection must be initialised with non-empty 'headers' argument.")
        for header in headers:
            setattr(self,header,[])

    def __len__(self):
        # get the first attr name in the keys of the object's __dict__
        # we assume all lists have the same length
        random_attr =  list(self.__dict__)[0]
        return len(getattr(self,random_attr))

    def __getitem__(self,key):
        if isinstance(key,slice):
            dc = DataCollection(list(self.__dict__))
            # the slice's 'indices' method returns a tuple with the start, step size and end
            # this can then be unpacked using * to pass them as arguments to 'range'
            for i in range(*key.indices(len(self))):
                dc.append(self[i])
            return dc
        return {header:value[key] for header,value in self.__dict__.items()}

    def append(self,d):
        for header, value in d.items():
            # shouldn't be a performance hit since it's all references in Python
            getattr(self,header).append(value)


class CSVParser(ABC):
    def parse(self, filename):
        records = []
        with open(filename) as f:
            rows = csv.reader(f)
            headers = next(rows)
            for row in rows:
                record = self.make_record(headers, row)
                records.append(record)
        return records

    @abstractmethod
    def make_record(self, headers, row):
        pass

class DictCSVParser(CSVParser):
    def __init__(self, types):
        self.types = types

    def make_record(self, headers, row):
        return {name: func(val) for name, func, val in zip(headers, self.types, row) }

class InstanceCSVParser(CSVParser):
    def __init__(self, cls):
        self.cls = cls

    def make_record(self, headers, row):
        return self.cls.from_row(row)

def read_csv_as_dicts(filename,coltypes):
    '''
    Parses a csv into a list of dictionaries with a specific
    type conversion mapping for each column.
    '''
    parser = DictCSVParser(coltypes)
    return parser.parse(filename)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    parser = InstanceCSVParser(cls)
    return parser.parse(filename)

def read_csv_as_columns(filename,types=None):
    '''
    General purpose CSV parser that stores data in a DataCollection object.
    '''
    assert type(types) != type(None), "Got no types for 'read_csv_as_columsn'"
    f = open(filename)
    rows = csv.reader(f)
    headers = next(rows)
    dc = DataCollection(headers)
    for row in rows:
        record = { name:func(val) for name, func, val in zip(headers,types,row) }
        dc.append(record)
    return dc
