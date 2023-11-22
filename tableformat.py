# tableformat.py


class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ') * len(headers))
    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        #print(','.join(str(h) for h in headers))
        print(','.join(headers)) # since these are string s already
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>',' '.join(f"<th>{h}</th>" for h in headers), '</tr>')
    def row(self, rowdata):
        print('<tr>',' '.join(f"<td>{d}</td>" for d in rowdata), '</tr>')

def create_formatter(fmt):
    if fmt == 'text':
        return TextTableFormatter()
    elif fmt == 'csv':
        return CSVTableFormatter()
    elif fmt == 'html':
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f'no formatter in format: {fmt} exists.')

def print_table(records, fields, formatter):
    '''
    Make a nicely formatted table showing object attributes.
    '''
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)

    #print('%10s '*len(attr_names) % tuple(attr_names))
    #print(('-'*10 + ' ') * len(attr_names))
    #for o in objects:
        #print('%10s '*len(attr_names) % tuple([str(getattr(o,name)) for name in attr_names]))
