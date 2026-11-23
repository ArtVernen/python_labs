
def bubble_sort(nums):
    """Сортировка пузырьком. Возвращает новый список."""
    result = list(nums)
    n = len(result)

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:
            break

    return result


def insertion_sort(nums):
    """Сортировка вставками. Возвращает новый список."""
    result = list(nums)

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0 and result[j] > current:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = current

    return result


def selection_sort(nums):
    """Сортировка выбором. Возвращает новый список."""
    result = list(nums)

    for i in range(len(result)):
        smallest = i
        for j in range(i + 1, len(result)):
            if result[j] < result[smallest]:
                smallest = j
        result[i], result[smallest] = result[smallest], result[i]

    return result
