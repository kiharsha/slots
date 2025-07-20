def TransposeMatrix(matrix1):
    if len(matrix1) < 0:
        return "matrices of different lengths cannot be transposed"

    rows = len(matrix1)
    cols = len(matrix1[0])
    result = [[0 for _ in range(rows)] for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix1[i][j]

    return result


matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

result_matrix = TransposeMatrix(matrix1)
for row in result_matrix:
    print(row)