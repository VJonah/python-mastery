# typedproperty.py

def typedproperty(expected_type):
    #private_name = '_' + name

    @my_property
    def value(self):
        return getattr(self, value.private_name)


    @value.setter
    def value(self, val):
        if not isinstance(val, expected_type):
            raise TypeError(f'Expected {expected_type}')
        setattr(self, value.private_name, val)

    return value

# thanks to https://github.com/dabeaz-course/python-mastery/issues/35
class my_property(property):
    def __set_name__(self, cls, name):
        self.private_name = '_' + name

String = lambda : typedproperty(str)
Integer = lambda : typedproperty(int)
Float = lambda : typedproperty(float)
#String  = lambda name: typedproperty(name,str)
#Integer  = lambda name: typedproperty(name,int)
#Float  = lambda name: typedproperty(name,float)
