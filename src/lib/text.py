
import re


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    """Приводит текст к нижнему регистру и убирает лишние пробелы."""
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")

    text = "".join(" " if ord(c) < 32 or ord(c) == 127 else c for c in text)
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    """Находит слова, в том числе слова с внутренним дефисом."""
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    """Считает количество появлений каждого слова."""
    freq = {}

    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """Сортирует по частоте по убыванию, затем по слову по алфавиту."""
    return sorted(freq.items(), key=lambda x: (-x[1], x[0]))[:max(0, n)]


if __name__ == "__main__":
    text = "ПрИвЕт\nМИр\t"

    print("=== normalize ===")
    print(
        f'"ПрИвЕт\\nМИр\\t" -> {normalize(text)}\n'
        f'"ёжик, Ёлка" -> {normalize("ёжик, Ёлка")}\n'
        f'"Hello World" -> {normalize("Hello World")}\n'
        f'"  двойные   пробелы  " -> {normalize("  двойные   пробелы  ")}'
    )

    print("\n=== tokenize ===")
    print(
        f'"привет мир" -> {tokenize("привет мир")}\n'
        f'"hello,world!!!" -> {tokenize("hello,world!!!")}\n'
        f'"по-настоящему круто" -> {tokenize("по-настоящему круто")}\n'
        f'"2025 год" -> {tokenize("2025 год")}\n'
        f'"emoji 😀 не слово" -> {tokenize("emoji 😀 не слово")}'
    )

    print("\n=== count_freq ===")
    print(
        f'["a", "b", "a", "c", "b", "a"] -> {count_freq(["a", "b", "a", "c", "b", "a"])}\n'
        f'["bb", "aa", "bb", "aa", "cc"] -> {count_freq(["bb", "aa", "bb", "aa", "cc"])}\n'
        f'[] -> {count_freq([])}'
    )

    print("\n=== top_n ===")
    print(
        f'n=2 -> {top_n({"a": 3, "b": 2, "c": 1}, 2)}\n'
        f'Равные частоты -> {top_n({"bb": 2, "aa": 2, "cc": 1}, 2)}\n'
        f'n=0 -> {top_n({"a": 3, "b": 2}, 0)}\n'
        f'Пустой словарь -> {top_n({}, 5)}'
    )