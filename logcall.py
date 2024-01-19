# logcall.py

from functools import wraps

def logformat(fmt):
    def logged(func):
        print('Adding logging to', func.__name__)
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(fmt.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged

#def logged(func):
   #return logformat('Calling {func.__name__}')(func)

logged = logformat('Calling {func.__name__}')