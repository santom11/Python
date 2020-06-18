'''
Decorators with and without arguments

1. If name has been called without arguments, the decorated function will be passed in as _func.
    If it has been called with arguments, then _func will be None, and some of the keyword arguments may
    have been changed from their default values. The * in the argument list means that the remaining arguments
    can’t be called as positional arguments.
2. In this case,the decorator was called with arguments. Return a decorator function that can read and return a function.
3. In this case,the decorator was called without arguments.Apply the decorator to the function immediately.
'''


def name(_func=None, *, kw1=val1, kw2=val2, ...):  # 1
    def decorator_name(func):
        ...  # Create and return a wrapper function.

    if _func is None:
        return decorator_name                      # 2
    else:
        return decorator_name(_func)               # 3


