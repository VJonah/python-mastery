# tableformat/formatter.py

from abc import ABC, abstractmethod

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class ColumnFormatMixin:
    formats = [] # class variable example!

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def create_formatter(fmt, column_formats=None, upper_headers=False):
    '''
    Creates a custom formatter by mixing in the right Mixin classes.
    '''
    if fmt == 'text':
        formatter_cls = TextTableFormatter
    elif fmt == 'csv':
        formatter_cls = CSVTableFormatter
    elif fmt == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError(f'no formatter in format: {fmt} exists.')

    # you probably don't need to do the combination of mixins (ie: no more than 1 mixin)
    if column_formats != None:
        if upper_headers == True:
            class formatter_cls(ColumnFormatMixin, UpperHeadersMixin, formatter_cls):
                formats = column_formats
        else:
            class formatter_cls(ColumnFormatMixin, formatter_cls):
                formats = column_formats
    elif upper_headers == True:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()

def print_table(records, fields, formatter):
    '''
    Make a nicely formatted table showing object attributes.
    '''
    if not isinstance(formatter,TableFormatter):
        raise TypeError('Exepcted a TableFormatter')
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

    #print('%10s '*len(attr_names) % tuple(attr_names))
    #print(('-'*10 + ' ') * len(attr_names))
    #for o in objects:
        #print('%10s '*len(attr_names) % tuple([str(getattr(o,name)) for name in attr_names]))
