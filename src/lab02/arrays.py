def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает минимальное и максимальное число."""
    if len(nums) == 0:
        raise ValueError("Список пуст")
    mn = nums[0]
    mx = nums[0]
    for x in nums:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx

def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает уникальные числа по возрастанию."""
    a = []
    k=-1
    for x in nums:
        if x not in a:
            a.append(x)
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                k=a[j]
                a[j]=a[j+1]
                a[j+1]=k
    return a


def flatten(mat: list[list | tuple]) -> list:
    """Превращает матрицу в один список."""
    a = []
    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("Строка должна быть списком или кортежем")
        for x in row:
            a.append(x)
    return a

#тест кейс
if __name__ == "__main__":
    print("min_max")
    print("[3, -1, 5, 5, 0] →", min_max([3, -1, 5, 5, 0]))
    print("[42] →", min_max([42]))
    print("[-5, -2, -9] →", min_max([-5, -2, -9]))
    print("[1.5, 2, 2.0, -3.1] →", min_max([1.5, 2, 2.0, -3.1]))
    try:
        print("[] →", min_max([]))
    except ValueError as e:
        print("[] →", e)
    print("unique_sorted")
    print("[3, 1, 2, 1, 3] →", unique_sorted([3, 1, 2, 1, 3]))
    print("[] →", unique_sorted([]))
    print("[-1, -1, 0, 2, 2] →", unique_sorted([-1, -1, 0, 2, 2]))
    print("[1.0, 1, 2.5, 2.5, 0] →", unique_sorted([1.0, 1, 2.5, 2.5, 0]))
    print("flatten")
    print("[[1, 2], [3, 4]] →", flatten([[1, 2], [3, 4]]))
    print("[[1, 2], (3, 4, 5)] →", flatten([[1, 2], (3, 4, 5)]))
    print("[[1], [], [2, 3]] →", flatten([[1], [], [2, 3]]))
    try:
        print('[[1, 2], "ab"] →', flatten([[1, 2], "ab"]))
    except TypeError as e:
        print('[[1, 2], "ab"] →', e)