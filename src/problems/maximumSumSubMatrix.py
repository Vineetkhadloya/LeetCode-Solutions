mat = [
        [3, -4, 6, -5, 1],
        [1, -2, 8, -4, -2],
        [3, -8, 9, 3, 1],
        [-7, 3, 4, 2, 7],
        [-3, 7, -5, 7, -6]
    ]
for i in mat:
    print(i)

processedMatrix = [[0 for i in range(len(mat))] for j in range(len(mat[0]))]
processedMatrix[0][0] = mat[0][0]
for j in range(1, len(mat[0])):
    processedMatrix[0][j] = mat[0][j] + processedMatrix[0][j - 1]

for j in range(1,len(mat)):
    processedMatrix[j][0] = mat[j][0] + processedMatrix[j-1][0]

for i in range(1,len(mat[0])):
    for j in range(1,len(mat[0])):
        processedMatrix[i][j] = mat[i][j] + processedMatrix[i-1][j] + processedMatrix[i][j-1] - processedMatrix[i-1][j-1]

print("-----------------------")
for i in processedMatrix:
    print(i)

k = 2
maximum = float("-inf")
op = {}
for i in range(k-1,len(mat)):
    for j in range(k-1,len(mat[0])):
        total = processedMatrix[i][j]

        if i-k >= 0:
            total -= processedMatrix[i-k][j]
        if j-k >= 0:
            total -= processedMatrix[i][j-k]
        if j-k >= 0 and i-k >= 0:
            total += processedMatrix[i-k][j-k]

        if total >= maximum:
            maximum = total
            if total in op.keys():
                op[total].append([i,j])
            else:
                op[total] = []
                op[total].append([i,j])

print(op[18])
op[18].append([44,44])

maxSubMatrix = op[max(op, key = op.get)]
print(maxSubMatrix)

a = set()

for i in maxSubMatrix:
    a.add(mat[i[0]])
    a.add(mat[i[1]])

print(op)