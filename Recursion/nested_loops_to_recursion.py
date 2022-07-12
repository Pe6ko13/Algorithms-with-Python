def nested_loop(idx, arr):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return
    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loop(idx + 1, arr)

n = int(input())
arr = [None] * n

nested_loop(0, arr)