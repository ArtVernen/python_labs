
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n


TABLE_MODE = False  # True — вывести дополнительную таблицу ★


def main() -> None:
    text = input()
    words = tokenize(normalize(text))
    freq = count_freq(words)

    print("Всего слов:", len(words))
    print("Уникальных слов:", len(freq))
    print("Топ-5:")

    top = top_n(freq, 5)

    for word, count in top:
        print(f"{word}:{count}")

    if TABLE_MODE:
        width = max([len("слово")] + [len(word) for word, count in top])

        print(f"{'слово':<{width}} | частота")
        print("-" * (width + 10))

        for word, count in top:
            print(f"{word:<{width}} | {count}")


if __name__ == "__main__":
    main()
