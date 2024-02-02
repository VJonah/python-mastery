# tableformat/formats/csv.py

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        #print(','.join(str(h) for h in headers))
        print(','.join(headers)) # since these are string s already
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
