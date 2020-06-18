##Decorator with and without arguments

from Decorators.decorators import repeat_1, slowdown


@repeat_1()
def say_whee():
    print("Whee!!")

say_whee()


@repeat_1(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("Santosh")


@slowdown(rate=2)
def countdown(numb):
    if numb < 1:
        print( f"Number is smaller than 1")
    else:
        print(numb)
        countdown(numb - 1)

countdown(10)