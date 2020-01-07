matrix = [
    [1, 0, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0]
]
haveVisited = [[False for column in range(len(matrix))] for rows in range(len(matrix[0]))]
print(haveVisited)

queue = []
for column in range(len(matrix)):
    for row in range(len(matrix[column])):
        if matrix[column][row] == 1:
            queue.append([column, row])

result = []
for i in range(len(queue)):
    if queue[i] == [-10, -10]:
        continue
    j = i + 1
    counter = 1
    while j < len(queue):
        if queue[i][0] + 1 == queue[j][0] and queue[i][1] == queue[j][1]:
            counter += 1
            queue[i][0] = queue[j][0]
            queue[j] = [-10, -10]
        if queue[i][1] + 1 == queue[j][1] and queue[i][0] == queue[j][0]:
            counter += 1
            queue[i][1] = queue[j][1]
            queue[j] = [-10, -10]
        j += 1
    result.append(counter)

print(sorted(result))