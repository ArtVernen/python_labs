
import random

from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

checks = 0


def check_sorting(fn, trials=100):
    """Сравнивает сортировку с sorted и проверяет исходный список."""
    global checks

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        assert fn(nums) == sorted(nums), f"Ошибка сортировки: {fn.__name__}, {nums}"
        assert nums == original, f"Изменился исходный список: {fn.__name__}, {nums}"
        checks += 1

    for nums in ([], [5], [2, 1], [3, 3, 1]):
        original = list(nums)
        assert fn(nums) == sorted(nums), f"Ошибка сортировки: {fn.__name__}, {nums}"
        assert nums == original, f"Изменился исходный список: {fn.__name__}, {nums}"
        checks += 1


def check_search():
    """Проверяет линейный и бинарный поиск на случайных списках."""
    global checks

    for _ in range(100):
        n = random.randint(0, 50)
        nums = [random.randint(-20, 20) for _ in range(n)]
        x = random.randint(-25, 25)

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        assert linear_search(nums, x) == expected, f"Ошибка linear_search: {nums}, x={x}"
        checks += 1

        ordered = sorted(nums)
        index = binary_search(ordered, x)

        if x in ordered:
            assert index != -1 and ordered[index] == x, f"Ошибка binary_search: {ordered}, x={x}"
        else:
            assert index == -1, f"Ошибка binary_search: {ordered}, x={x}"
        checks += 1

        if ordered:
            for edge in (ordered[0], ordered[-1]):
                index = binary_search(ordered, edge)
                assert index != -1 and ordered[index] == edge, f"Не найден крайний элемент: {ordered}"
                checks += 1

    assert linear_search([], 5) == -1
    assert binary_search([], 5) == -1
    assert binary_search([5], 5) == 0
    assert binary_search([1, 3], 2) == -1
    checks += 4


def check_two_sum(trials=100):
    """Проверяет, что оба способа находят правильную пару или None."""
    global checks

    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        assert (brute is None) == (fast is None), f"Разные результаты: {nums}, {target}"

        for pair in (brute, fast):
            if pair is not None:
                i, j = pair
                assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target, (
                    f"Неверная пара: {nums}, {target}, {pair}"
                )
        checks += 1

    for nums, target in (([2, 7, 11, 15], 9), ([3, 3], 6), ([1, 2], 10), ([], 0)):
        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        assert (brute is None) == (fast is None)

        for pair in (brute, fast):
            if pair is not None:
                i, j = pair
                assert 0 <= i < j < len(nums) and nums[i] + nums[j] == target
        checks += 1


def main():
    random.seed(42)

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)

    check_search()
    check_two_sum()

    print(f"OK: {checks} проверок")


if __name__ == "__main__":
    main()
