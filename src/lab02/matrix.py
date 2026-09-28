def check_matrix(mat):
    """Проверяет, что строки матрицы одинаковой длины."""
    if len(mat) == 0:
        return
    n = len(mat[0])
    for row in mat:
        if len(row) != n:
            raise ValueError("Матрица рваная")


def transpose(mat: list[list[float | int]]) -> list[list]:
    """Меняет строки и столбцы местами."""
    check_matrix(mat)
    if len(mat) == 0:
        return []
    res = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        res.append(row)
    return res


def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Считает сумму каждой строки."""
    check_matrix(mat)
    res = []
    for row in mat:
        s = 0
        for x in row:
            s += x
        res.append(s)
    return res


def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Считает сумму каждого столбца."""
    check_matrix(mat)
    if len(mat) == 0:
        return []
    res = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s += mat[i][j]
        res.append(s)
    return res


#тест кейс
if __name__ == "__main__":
    print("check_matrix")
    print(check_matrix([[1, 2], [3, 4]]))
    print(check_matrix([[1, 2, 3], [4, 5, 6]]))
    print(check_matrix([]))
    print(check_matrix([[1, 2], [3]]))