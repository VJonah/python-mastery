# tableformat/formatter.py

from abc import ABC, abstractmethod

class TableFormatter(ABC):
    _formats = {}

    @classmethod
    def __init_subclass__(cls):
        name = cls.__module__.split('.')[-1]
        TableFormatter._formats[name] = cls

    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass



class ColumnFormatMixin:
    formats = [] # class variable example!

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)

class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])

def create_formatter(name, column_formats=None, upper_headers=False):
    '''
    Creates a custom formatter by mixing in the right Mixin classes.
    '''
    if name not in TableFormatter._formats:
        __import__(f'{__package__}.formats.{name}')

    formatter_cls = TableFormatter._formats.get(name)
    if not formatter_cls:
        raise RuntimeError('Unknown format %s' % name)

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
