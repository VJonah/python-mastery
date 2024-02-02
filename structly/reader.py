# reader.py
import csv
from typing import List
import logging
log = logging.getLogger(__name__)

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
    make_dict = lambda headers, row: {name: func(val) for name, func, val in zip(headers, types, row)}
    return convert_csv(lines, make_dict, headers=headers)

def csv_as_instances(lines:iter, cls: type, *, headers: List[str] = None) -> List[type]:
    '''
    Parse CSV lines of an iterable object into a list of class instances.
    '''
    records = []
    rows = csv.reader(lines)
    make_instance = lambda _, row: cls.from_row(row)
    return convert_csv(lines, make_instance, headers=headers)

def convert_csv(lines:iter, conversion_func, *, headers=None) -> list:
    '''
    Convert a CSV lines of an iterable object based on a given row parsing function.
    '''
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)

    records = []
    for i,row in enumerate(rows,start=1):
        try:
            records.append(conversion_func(headers, row))
        except ValueError as e:
            log.warning(f'Bad row: {row}')
            log.debug(f'Reason: {e}')

    return records
