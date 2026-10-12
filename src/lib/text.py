
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
