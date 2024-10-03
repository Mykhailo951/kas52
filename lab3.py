def count_num (a, b):
    count = 0
    for num in range(a, b + 1):
        if '5' not in str(num):
            count += 1
    return count

print(count_num(1, 200))

