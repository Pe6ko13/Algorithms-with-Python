def calc_fact(n):
    if n == 1:
        return 15
    return n * calc_fact(n-1)

n = int(input())

print(calc_fact(n))