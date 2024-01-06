# structure.py

class Structure:
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError(f'Expected {len(self._fields)} arguments')

        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)

    def __repr__(self):
        return f"{self.__class__.__name__}({','.join(repr(getattr(self,name)) for name in self._fields)})"

    def __setattr__(self, name, value):
        if not name.startswith('_') and name not in self._fields:
            raise AttributeError(f'No attribute {name}')
        super().__setattr__(name, value)
