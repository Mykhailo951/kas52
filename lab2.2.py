a, b, h = 1, 1.5, 0.05

d = 10**(-5)

def sum(x, d):
    n = 1
    term = (x - 1)**n / (n * x**n)
    sum = term

    while abs(term) > d:
        n += 1
        term = (x - 1)**n / (n * x**n)
        sum += term
    return sum

def tb(a, b, h, d):
    x = a
    res = []

    while x <= b:
        y = sum(x, d)
        res.append((x, y))
        x += h
        x = round(x, 2)
        print(x)
    return res

res = tb(a, b, h, d)
for x, y in res:
    print(x, y)
