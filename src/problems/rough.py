def findMissing(nums,matrix):
    print(" In findMissing")
    print(matrix)
    contains = set()

    for i in matrix:
        print(i)
        contains |= set(i)
    print(contains)

    return 0


matrices = [
["1", "2", "3", "4","?", "5", "6", "10"],
["1", "2", "3", "4","11", "5", "6", "10"],
["1", "2", "3", "4","12", "5", "6", "10"]
]
print(len(matrices))
a = []
for j in range(0,len(matrices[0]),4):
    x = []
    for i in range(len(matrices)):
        x.append(matrices[i][j:j+4])
        print(matrices[i][j:j+4])
    print(x)
    a.append(x)

print(a)
nums = set('?') | set([str(i) for i in range(1,17)])
print(nums)

for i,matrix in enumerate(a):
    missingNum = findMissing(nums,matrix)