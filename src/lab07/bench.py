
import random
import timeit
from pathlib import Path

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import linear_search, binary_search, two_sum_brute, two_sum_fast
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def make_data(n):
    """Создаёт список случайных чисел."""
    return [random.randint(0, n * 10) for _ in range(n)]


def bench_sorts(n):
    """Измеряет время разных сортировок на одном списке."""
    nums = make_data(n)
    rows = []

    seconds = timeit.timeit(lambda: sorted(nums), number=1)
    rows.append(("sort", n, "sorted", seconds))

    for name, fn in (("bubble", bubble_sort),
                     ("insertion", insertion_sort),
                     ("selection", selection_sort)):
        if n == 100_000:
            rows.append(("sort", n, name, "не измерялось"))
        else:
            seconds = timeit.timeit(lambda: fn(nums), number=1)
            rows.append(("sort", n, name, seconds))

    return rows


def bench_search():
    """Сравнивает 10 000 поисков в списке из 100 000 элементов."""
    nums = make_data(100_000)
    queries = [random.choice(nums) for _ in range(10_000)]
    rows = []

    def run_linear():
        for x in queries:
            linear_search(nums, x)

    seconds = timeit.timeit(run_linear, number=1)
    rows.append(("search", 100_000, "linear", seconds))

    sort_seconds = timeit.timeit(lambda: sorted(nums), number=1)
    ordered = sorted(nums)

    def run_binary():
        for x in queries:
            binary_search(ordered, x)

    seconds = timeit.timeit(run_binary, number=1)

    rows.append(("search", 100_000, "sort_before_binary", sort_seconds))
    rows.append(("search", 100_000, "binary", seconds))
    rows.append(("search", 100_000, "binary_with_sort", sort_seconds + seconds))

    return rows


def bench_two_sum(n):
    """Сравнивает поиск пары двумя способами."""
    nums = [random.randint(1, 100_000) for _ in range(n - 2)]
    nums += [500_000, 500_001]
    target = 1_000_001
    rows = []

    seconds = timeit.timeit(lambda: two_sum_brute(nums, target), number=1)
    rows.append(("two_sum", n, "brute", seconds))

    seconds = timeit.timeit(lambda: two_sum_fast(nums, target), number=1)
    rows.append(("two_sum", n, "fast", seconds))

    return rows


def print_table(rows):
    print(f"{'task':<10} {'n':>8} {'impl':<20} {'seconds':>16}")
    print("-" * 58)

    for task, n, impl, seconds in rows:
        if isinstance(seconds, float):
            seconds = f"{seconds:.6f}"
        print(f"{task:<10} {n:>8} {impl:<20} {seconds:>16}")


def main():
    random.seed(42)
    rows = []

    for n in (1_000, 10_000, 100_000):
        rows += bench_sorts(n)

    rows += bench_search()

    for n in (1_000, 10_000):
        rows += bench_two_sum(n)

    print_table(rows)

    Path("data/lab07").mkdir(parents=True, exist_ok=True)

    csv_rows = []

    for task, n, impl, seconds in rows:
        if isinstance(seconds, float):
            seconds = f"{seconds:.6f}"
        csv_rows.append((task, n, impl, seconds))

    write_csv(
        csv_rows,
        "data/lab07/bench.csv",
        header=("task", "n", "impl", "seconds")
    )

    print("\nРезультаты сохранены в data/lab07/bench.csv")


if __name__ == "__main__":
    main()
