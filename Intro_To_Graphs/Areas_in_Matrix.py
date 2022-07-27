def dfs(row, col, parent, matrix, visited):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
            return
    if visited[row][col]:
        return
    if matrix[row][col] != parent:
        return

    visited[row][col] = True
    dfs(row, col - 1, parent, matrix, visited)
    dfs(row, col + 1, parent, matrix, visited)
    dfs(row - 1, col, parent, matrix, visited)
    dfs(row + 1, col, parent, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []
areas = {}
total_areas = 0

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

for row in range(rows):
    for col in range(cols):
        if visited[row][col] == True:
            continue
        parent = matrix[row][col]
        dfs(row, col, parent, matrix, visited)
        if parent not in areas:
            areas[parent] = 1

        else:
            areas[parent] += 1

        total_areas += 1

print(f"Areas: {total_areas}")
for area, size in sorted(areas.items()):
    print(f"Letter '{area}' -> '{size}'")