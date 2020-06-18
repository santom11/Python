from Decorators.decorators import do_twice
from Decorators.decorators import timer, slow_down, repeat


@do_twice
def say_whee():
    print("whee!")

say_whee()


@timer
def time_cal(time_interval):
    for _ in range(time_interval):
        sum([i**2 for i in range(1000)])

time_cal(1)
time_cal(1000)


@slow_down
def count_down(interval):
    if interval < 1:
        print( "Less than 1 assigned" )
    else:
        print(interval)
        count_down(interval - 1)

count_down(6)



## Decorator with Argument & double decorators

@repeat(num_times=4)
@slow_down
def greet(name):
    print( f"Hello {name}")

greet("santosh")