from collections import deque

words = input().split()

size = [0] * len(words)
prev = [None] * len(words)

best_size = 0
best_idx = 0

for i in range(len(words)):
    curr_word = words[i]
    curr_size = 1
    parent = None

    for prev_i in range(i - 1, -1, -1):
        prev_word = words[prev_i]

        if len(prev_word) >= len(curr_word):
            continue
        if size[prev_i] + 1 >= curr_size:
            curr_size = size[prev_i] + 1
            parent = prev_i

    size[i] = curr_size
    prev[i] = parent

    if curr_size > best_size:
        best_size = curr_size
        best_idx = i

lis = deque()

idx = best_idx
while idx is not None:
    lis.appendleft(words[idx])
    idx = prev[idx]

print(*lis, sep=' ')