import csv
import sys
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает текст из файла."""
    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(rows: list[tuple | list], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Записывает данные в CSV."""
    if rows:
        length = len(rows[0])

        for row in rows:
            if len(row) != length:
                raise ValueError("Строки разной длины")

        if header is not None and len(header) != length:
            raise ValueError("Длина заголовка не совпадает с длиной строк")

    file = Path(path)
    file.parent.mkdir(parents=True, exist_ok=True)

    with file.open("w", newline="", encoding="utf-8") as f: 
        w = csv.writer(f)

        if header is not None:
            w.writerow(header)

        w.writerows(rows)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = "data/lab04/input.txt"
    text = read_text(path)

    if text:
        print(text)

    if len(sys.argv) == 1:
        write_csv(
            [("привет", 2), ("мир", 1)],
            "data/lab04/check.csv",
            ("word", "count")
        )