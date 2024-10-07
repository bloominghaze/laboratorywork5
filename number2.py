size = 7
matrix = [[0] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        min_distance = min(i, size - i - 1)
        matrix[i][j] = 4 + min_distance

for row in matrix:
    print(' '.join(map(str, row)))
