# structure.py

from validate import Validator, validated
from collections import ChainMap


class StructureMeta(type):
    @classmethod
    def __prepare__(meta, clsname, bases):
        return ChainMap({}, Validator.validators)

    @staticmethod
    def __new__(meta, name, bases, methods):
        methods = methods.maps[0]
        return super().__new__(meta, name, bases, methods)

class Structure(metaclass=StructureMeta):
    _types = ()
    _fields = () # why is this necessary? In case we forget to initialise one in the subclass?

    @classmethod
    def __init_subclass__(cls):
        validate_attributes(cls)

    @classmethod
    def create_init(cls):
        argstr = ','.join(cls._fields)
        code = f'def __init__(self,{argstr}):\n'
        for name in cls._fields:
            code += f'    self.{name} = {name}\n'
        locs = { }
        exec(code, locs)
        cls.__init__ = locs['__init__']

    @classmethod
    def from_row(cls, row):
        rowdata = [ func(val) for func, val in zip(cls._types, row)]
        return cls(*rowdata)

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

def validate_attributes(cls):
    '''
    Class decorator that scans a class definition for Validators
    and builds a _fields variable that captures their definition order.
    '''
    validators = []
    for name, val in vars(cls).items():
        if isinstance(val, Validator):
            validators.append(val)

        # Apply validated decorator to any callable with annotations
        elif callable(val) and val.__annotations__:
            setattr(cls, name, validated(val))
    cls._fields = tuple(val.name for val in validators)
    cls._types = tuple(getattr(val, 'expected_type', lambda x : x) for val in validators)
    cls.create_init()
    return cls

def typed_structure(clsname, **validators):
    cls = type(clsname, (Structure,), validators)
    return cls
