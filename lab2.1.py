from math import atan, log, tan

a = -0.9
b = -0.4
h = 0.05



def fun1(x):
    return atan(x**3)


def fun2(x):
    return tan(x + log(abs(x)))

def fun3(x):
    return 1 / tan(x**2)

def tb(a, b, h):
    x = a
    res = []

    while x <= b:
        if x <= -0.7:
            y = fun1(x)
        elif -0.7 < x <= -0.6:
            y = fun2(x)
        else:
            y = fun3(x)

        res.append((x, y))
        x += h

    return res

res = tb(a, b, h)

for x, y in res:
    print(x, y)