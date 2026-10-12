
import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Читает содержимое текстового файла."""
    return Path(path).read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создаёт родительские папки для файла, если их нет."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None
) -> None:
    """Записывает CSV и проверяет одинаковое количество столбцов."""

    if header is not None:
        width = len(header)
    elif rows:
        width = len(rows[0])
    else:
        width = None

    for row in rows:
        if width is not None and len(row) != width:
            raise ValueError("Все строки должны иметь одинаковое число столбцов")

    ensure_parent_dir(path)

    with Path(path).open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)
