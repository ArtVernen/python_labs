# Лабораторная работа №2

В работе используются списки, кортежи и матрицы.

Ограничения:
- без `min()` и `max()`;
- без `sorted()` и `.sort()`;
- сортировка и подсчёт сумм выполняются вручную.

---

## 1. Работа со списками — `arrays.py`

### `min_max`

Возвращает минимальное и максимальное число списка.

```python
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
```

### `unique_sorted`

Удаляет повторяющиеся элементы и сортирует список по возрастанию без `sorted()` и `.sort()`.

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает уникальные числа по возрастанию."""
    a = []
    k = -1

    for x in nums:
        if x not in a:
            a.append(x)

    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                k = a[j]
                a[j] = a[j + 1]
                a[j + 1] = k

    return a
```

### `flatten`

Объединяет списки и кортежи в один список.

```python
def flatten(mat: list[list | tuple]) -> list:
    """Превращает матрицу в один список."""
    a = []

    for row in mat:
        if type(row) != list and type(row) != tuple:
            raise TypeError("Строка должна быть списком или кортежем")

        for x in row:
            a.append(x)

    return a
```

### Тестирование

![Тестирование arrays.py](../../images/lab02/arrays.png)

---

## 2. Работа с матрицами — `matrix.py`

### `check_matrix`

Проверяет, что все строки матрицы имеют одинаковую длину.

```python
def check_matrix(mat):
    """Проверяет, что строки матрицы одинаковой длины."""
    if len(mat) == 0:
        return

    n = len(mat[0])

    for row in mat:
        if len(row) != n:
            raise ValueError("Матрица рваная")
```

### `transpose`

Меняет строки и столбцы матрицы местами.

```python
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
```

### `row_sums`

Считает сумму элементов каждой строки.

```python
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
```

### `col_sums`

Считает сумму элементов каждого столбца.

```python
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
```

### Тестирование

![Тестирование matrix.py](../../images/lab02/matrix.png)

---

## 3. Работа с кортежами — `tuples.py`

### `format_record`

Получает кортеж с ФИО, группой и GPA и формирует строку с фамилией, инициалами, группой и средним баллом.

Также выполняется проверка входных данных.

```python
def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись о студенте."""
    if type(rec) != tuple:
        raise TypeError("Запись должна быть кортежем")

    if len(rec) != 3:
        raise ValueError("В записи должно быть 3 элемента")

    fio = rec[0]
    group = rec[1]
    gpa = rec[2]

    if type(fio) != str or type(group) != str:
        raise TypeError("ФИО и группа должны быть строками")

    if type(gpa) != int and type(gpa) != float:
        raise TypeError("GPA должен быть числом")

    parts = fio.split()
    group = group.strip()

    if len(parts) < 2:
        raise ValueError("Неверное ФИО")

    if group == "":
        raise ValueError("Группа пустая")

    if gpa < 0 or gpa > 5:
        raise ValueError("GPA должен быть от 0 до 5")

    surname = parts[0].capitalize()
    initials = ""

    for i in range(1, len(parts)):
        if i > 2:
            break

        initials += parts[i][0].upper() + "."

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
```

### Тестирование

![Тестирование tuples.py](../../images/lab02/tuples.png)

