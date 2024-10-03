from math import atan, log, tan

a, b, h = -0.9, -0.4, 0.05

def tb(a, b, h):
    x, res = a, []

    while x <= b:
        if x <= -0.7:
            y = atan(x**3)
        elif -0.7 < x <= -0.6:
            y = tan(x + log(abs(x)))
        else:
            y = 1 / tan(x**2)

        res.append((x, y))
        x += h
        x = round(x, 2)
        print(x)
    return res

res = tb(a, b, h)
for x, y in res:
    print(x, y)
