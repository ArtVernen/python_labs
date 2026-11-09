
import argparse
from pathlib import Path

from src.lib.text import normalize, tokenize, count_freq, top_n


def cat_command(input_path, numbers=False):
    with open(input_path, "r", encoding="utf-8") as file:
        for number, line in enumerate(file, 1):
            if numbers:
                print(f"{number} {line}", end="")
            else:
                print(line, end="")


def stats_command(input_path, top=5):
    text = Path(input_path).read_text(encoding="utf-8")

    words = tokenize(normalize(text))
    freq = count_freq(words)

    print(f"Всего слов: {len(words)}")
    print(f"Уникальных слов: {len(freq)}")
    print(f"Топ-{top}:")

    for word, count in top_n(freq, top):
        print(f"{word}:{count}")


def main():
    parser = argparse.ArgumentParser(description="Работа с текстом")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cat = subparsers.add_parser("cat", help="Вывод файла")
    cat.add_argument("--input", required=True)
    cat.add_argument("-n", action="store_true")

    stats = subparsers.add_parser("stats", help="Статистика слов")
    stats.add_argument("--input", required=True)
    stats.add_argument("--top", type=int, default=5)

    args = parser.parse_args()

    if args.command == "stats" and args.top < 1:
        parser.error("--top должен быть больше 0")

    try:
        if args.command == "cat":
            cat_command(args.input, args.n)
        elif args.command == "stats":
            stats_command(args.input, args.top)
    except FileNotFoundError:
        parser.error("Файл не найден")
    except UnicodeDecodeError:
        parser.error("Неверная кодировка файла")


if __name__ == "__main__":
    main()
