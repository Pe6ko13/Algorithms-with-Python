def fibo(num):
    if num <= 1:
        return 1
    return fibo(num - 1) + fibo(num - 2)


def fibo2(num):
    f0 = 1
    f1 = 1
    result = 0
    for _ in range(num - 1):
        result = f0 + f1
        f0, f1 = f1, result
    return result

# print(fibo(int(input())))

print(fibo2(int(input())))