import functools
import time

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def slow_down(func):
    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)
    return wrapper_slow_down


## Decorators with Arguments
## num_times is the argument passed here
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat


# Decorator with and without arguments

def repeat_1(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat_1(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat_1

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)


## slow down decorator with additional arguments

def slowdown(_func=None, *, rate=2):
    def decorator_slowdown(func):
        @functools.wraps(func)
        def wrapper_slowdown(*args, **kwargs):
            time.sleep(rate)
            return func(*args, **kwargs)
        return wrapper_slowdown

    if _func is None:
        return decorator_slowdown
    else:
        return decorator_slowdown(_func)



