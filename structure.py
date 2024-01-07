# structure.py

import sys
import inspect

class Structure:
    _fields = () # why is this necessary? In case we forget to initialise one in the subclass?

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self,{argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = { }
        exec(code, locs)
        cls.__init__ = locs['__init__']

    def __repr__(self):
        return f"{self.__class__.__name__}({', '.join(repr(getattr(self, name)) for name in self._fields)})"

    def __setattr__(self, name, value):
        if not name.startswith('_') and name not in self._fields:
            raise AttributeError(f'No attribute {name}')
        super().__setattr__(name, value)

# a note on the __setattr__ method
# it works because the method resolution order (MRO) of a
# child to Structure will use the __setattr__ of builtins.object
# which behaves as expected! Lesson: always consider differing to super()!
