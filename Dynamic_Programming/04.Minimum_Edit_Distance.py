replacement = int(input())
insert = int(input())
delete = int(input())
first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1

dp = []
for _ in range(rows):
    dp.append([0] * cols)

for col in range(1, cols):
    dp[0][col] = dp[0][col - 1] + insert

for row in range(1, rows):
    dp[row][0] = dp[row - 1][0] + delete

for row in range(1, rows):
    for col in range(1, cols):
        if first[row - 1] == second[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1] + insert, dp[row - 1][col] + delete, dp[row - 1][col - 1] + replacement)

print(f"Minimum edit distance: {dp[rows - 1][cols - 1]}")
