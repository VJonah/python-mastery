# tableformat/formats/html.py

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>',' '.join(f"<th>{h}</th>" for h in headers), '</tr>')
    def row(self, rowdata):
        print('<tr>',' '.join(f"<td>{d}</td>" for d in rowdata), '</tr>')
