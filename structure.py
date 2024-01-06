# structure.py

class Structure:
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        for i, field in enumerate(self._fields):
            setattr(self, field, args[i])

    def __repr__(self):
        return f"{self.__class__.__name__}({','.join([str(v) if not isinstance(v,str) else repr(v) for _, v in self.__dict__.items()])})"

    def __setattr__(self, name, value):
        if name[0] != '_' and name not in self._fields:
            raise AttributeError(f'No attribute {name}')
        self.__dict__[name] = value

class Stock(Structure):
    _fields = ('name','shares','price')

s = Stock('GOOG',100,490.1)