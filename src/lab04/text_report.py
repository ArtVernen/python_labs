import sys

from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv


def main():
    """Считает частоту слов и сохраняет CSV-отчёт."""
    path = sys.argv[1] if len(sys.argv) > 1 else "data/lab04/input.txt"
    encoding = sys.argv[2] if len(sys.argv) > 2 else "utf-8"

    text = read_text(path, encoding)

    words = tokenize(normalize(text))
    freq = count_freq(words)

    rows = sorted(freq.items(), key=lambda x: (-x[1], x[0]))

    write_csv(rows, "data/lab04/report.csv", ("word", "count"))

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top_n(freq, 5):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()