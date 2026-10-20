import re


def normalize(text: str) -> str:
    text = text.casefold().replace("ё", "е")
    return " ".join(text.split())


def tokenize(text: str) -> list[str]:
    return re.findall(r"\w+(?:-\w+)*", text)


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for word in tokens:
        freq[word] = freq.get(word, 0) + 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    words = sorted(freq.items(), key=lambda item: (-item[1], item[0]))
    return words[:n]