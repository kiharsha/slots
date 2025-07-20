def MultiplyMatrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) and len(matrix1[0]) != len(matrix2[0]):
        return "matrices of different lengths cannot be added"

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] * matrix2[i][j])
        result.append(row)

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [1, 2, 3]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = MultiplyMatrices(matrix1,matrix2)
for row in result_matrix:
    print(row)