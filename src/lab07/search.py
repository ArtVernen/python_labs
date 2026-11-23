
def linear_search(nums, x):
    """Возвращает индекс первого x в списке или -1."""
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums, x):
    """Ищет x в отсортированном списке. Если x нет, возвращает -1.
    На неотсортированном списке результат не определён.
    """
    left = 0
    right = len(sorted_nums) - 1

    while left <= right:
        middle = (left + right) // 2
        if sorted_nums[middle] == x:
            return middle
        elif sorted_nums[middle] < x:
            left = middle + 1
        else:
            right = middle - 1

    return -1


def two_sum_brute(nums, target):
    """Перебирает пары и возвращает их индексы или None."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums, target):
    """Ищет пару за один проход с помощью словаря."""
    seen = {}

    for i in range(len(nums)):
        needed = target - nums[i]
        if needed in seen:
            return (seen[needed], i)
        seen[nums[i]] = i

    return None
