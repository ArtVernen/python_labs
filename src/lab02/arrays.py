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
    print("flatten")
    print("[[1, 2], [3, 4]] →", flatten([[1, 2], [3, 4]]))
    print("[[1, 2], (3, 4, 5)] →", flatten([[1, 2], (3, 4, 5)]))
    print("[[1], [], [2, 3]] →", flatten([[1], [], [2, 3]]))
    print(flatten([[1, 2], "ab"]))