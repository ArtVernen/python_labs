
import csv
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
        writer = csv.writer(f)

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)
