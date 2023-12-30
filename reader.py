# reader.py
import csv
from typing import List

def read_csv_as_dicts(filename: str, types: List[type], *, headers: List[str] = None) -> List[dict]:
    '''
    Read CSV data into a list of dictionaries with optional type conversion
    '''
    with open(filename) as file:
        return csv_as_dicts(file, types, headers=headers)

def read_csv_as_instances(filename: str, cls: type, *,  headers: List[str] = None) -> List[type]:
    '''
    Read CSV data into a list of instances
    '''
    with open(filename) as file:
        return csv_as_instances(file, cls, headers=headers)

def csv_as_dicts(lines: iter, types: List[type], *, headers: List[str] = None) -> List[dict]:
    '''
    Parse CSV lines of an iterable object into a list of dictionary records.
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = {name: func(val) for name, func, val in zip(headers, types, row)}
        records.append(record)
    return records

def csv_as_instances(lines:iter, cls: type, *, headers: List[str] = None) -> List[type]:
    '''
    Parse CSV lines of an iterable object into a list of class instances.
    '''
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        record = cls.from_row(row)
        records.append(record)
    return records
