import inspect

a = 5
b = 7
c = 22


def func(a, b, c):
    pass

x = len(inspect.getfullargspec(func).args)

print(inspect.getfullargspec(func).args[0])