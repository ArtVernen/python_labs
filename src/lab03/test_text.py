
import io
import sys
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.text import normalize, tokenize, count_freq, top_n
from lab03 import text_stats


def check(label, actual, expected):
    assert actual == expected, f"{label}: ожидалось {expected!r}, получено {actual!r}"
    print(f"{label} -> {actual!r}")


def run_program(text: str, table: bool = False) -> str:
    output = io.StringIO()

    with patch("builtins.input", return_value=text):
        with patch.object(text_stats, "TABLE_MODE", table):
            with redirect_stdout(output):
                text_stats.main()

    return output.getvalue()


def main():
    print("=== normalize ===")

    for text, expected in [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("  двойные   пробелы  ", "двойные пробелы"),
        ("", ""),
        ("a\x00b", "a b"),
    ]:
        check(repr(text), normalize(text), expected)

    check("yo2e=False", normalize("Ёжик", yo2e=False), "ёжик")
    check("casefold=False", normalize("Straße", casefold=False), "straße")

    print("\n=== tokenize ===")

    for text, expected in [
        ("привет, мир!", ["привет", "мир"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
        ("", []),
    ]:
        check(repr(text), tokenize(text), expected)

    print("\n=== count_freq ===")

    tokens = ["a", "b", "a", "c", "b", "a"]
    freq = count_freq(tokens)

    check(repr(tokens), freq, {"a": 3, "b": 2, "c": 1})
    check("[]", count_freq([]), {})

    print("\n=== top_n ===")

    check("n=2", top_n(freq, 2), [("a", 3), ("b", 2)])
    check("n=5", top_n(freq, 5), [("a", 3), ("b", 2), ("c", 1)])
    check(
        "равные частоты",
        top_n({"bb": 2, "aa": 2}, 2),
        [("aa", 2), ("bb", 2)]
    )
    check("n=0", top_n(freq, 0), [])
    check("пустой словарь", top_n({}, 5), [])

    print("\n=== text_stats.py ===")

    result = run_program("Привет, мир! Привет!!!")
    expected = (
        "Всего слов: 3\n"
        "Уникальных слов: 2\n"
        "Топ-5:\n"
        "привет:2\n"
        "мир:1\n"
    )

    assert result == expected
    print("Ввод: 'Привет, мир! Привет!!!'")
    print(result, end="")

    print("\n=== Пустой текст ===")

    result = run_program("")
    expected = "Всего слов: 0\nУникальных слов: 0\nТоп-5:\n"

    assert result == expected
    print(result, end="")

    print("\n=== Таблица ★ ===")

    result = run_program("Привет мир привет", table=True)

    assert "привет | 2" in result
    assert "мир" in result
    assert "частота" in result

    print(result, end="")


if __name__ == "__main__":
    main()
