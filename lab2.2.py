a = 1
b = 1.5
h = 0.05
d = 10**(-5)


def s_s(x, d):
    n = 1
    term = (x - 1)**n / (n * x**n)
    s_s = term

    while abs(term) > d:
        n += 1
        term = (x - 1)**n / (n * x**n)
        s_s += term

    return s_s


def tb(a, b, h, d):
    x = a
    res = []

    while x <= b:
        y = s_s(x, d)
        res.append((x, y))
        x += h

    return res


res = tb(a, b, h, d)
for x, y in res:
    print(x, y)