def missing_number(matrix, S):
    contains = set()
    for row in matrix:
        contains |= set(row)
        print("contains = ",contains)
    print("Hellooo")
    print(S - contains)
    missing_num = (S - contains).pop()
    print("missing num = ",missing_num)
    for row in matrix:
        if '?' in row:
            row[row.index("?")] = missing_num
            break
    return missing_num, matrix

def sort_matrices(matrices):
    S = set('?') | set([str(i) for i in list(range(1, 17))])
    print("S = ",set([str(i) for i in list(range(1, 17))]))
    print("S = ",S)
    res = []
    for i, matrix in enumerate(matrices):
        print("i = ",i)
        print("matrix = ",matrix)
        num, new_matrix = missing_number(matrix, S)
        res.append((num, i))
        print(res)
        matrices[i] = new_matrix
    res.sort()
    print(res)
    for num, i in res:
        print(matrices[i])

if __name__ == "__main__":
    matrices = [
               [["1", "2", "3", "4"],  ["?", "5", "6", "10"], ["13", "16", "12", "15"], ["9", "7", "8", "14"]], 
               [["1", "2", "3", "4"],  ["11", "5", "6", "10"], ["13", "16", "12", "15"], ["9", "?", "8", "14"]],
               [["1", "2", "3", "4"],  ["12", "5", "6", "10"], ["13", "16", "7", "15"], ["9", "?", "8", "14"]],
               ]
    sort_matrices(matrices)