def calc_binom(n, k, memo):
    key = f'{n} {k}'
    if key in memo:
        return memo[key]
    if n == 0 or k == 0 or n == k:
        return 1

    res = calc_binom(n -1, k - 1, memo) + calc_binom(n - 1, k, memo)
    memo[key] = res
    return res


n = int(input())
k = int(input())

print(calc_binom(n, k, {}))