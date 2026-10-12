
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


STAR_MODE = False  # True — обработать два файла ★
TABLE_MODE = False  # True — вывести таблицу ★
ENCODING = "utf-8"

INPUT_FILE = ROOT / "data" / "input.txt"

STAR_FILES = [
    ROOT / "data" / "a.txt",
    ROOT / "data" / "b.txt"
]


def main() -> None:
    files = STAR_FILES if STAR_MODE else [INPUT_FILE]

    total_freq = {}
    per_file_rows = []
    total_words = 0

    for path in files:
        text = read_text(path, encoding=ENCODING)
        words = tokenize(normalize(text))
        freq = count_freq(words)

        total_words += len(words)

        for word, count in freq.items():
            total_freq[word] = total_freq.get(word, 0) + count
            per_file_rows.append((path.name, word, count))

    if STAR_MODE:
        per_file_rows.sort(
            key=lambda row: (row[0], -row[2], row[1])
        )

        write_csv(
            per_file_rows,
            ROOT / "data" / "report_per_file.csv",
            header=("file", "word", "count")
        )

        write_csv(
            top_n(total_freq, len(total_freq)),
            ROOT / "data" / "report_total.csv",
            header=("word", "count")
        )

    else:
        write_csv(
            top_n(total_freq, len(total_freq)),
            ROOT / "data" / "report.csv",
            header=("word", "count")
        )

    print("Всего слов:", total_words)
    print("Уникальных слов:", len(total_freq))
    print("Топ-5:")

    for word, count in top_n(total_freq, 5):
        print(f"{word}:{count}")

    if TABLE_MODE:
        rows = top_n(total_freq, len(total_freq))

        width = max(
            [len("слово")] + [len(word) for word, count in rows]
        )

        print(f"{'слово':<{width}} | частота")
        print("-" * (width + 10))

        for word, count in rows:
            print(f"{word:<{width}} | {count}")


if __name__ == "__main__":
    main()
