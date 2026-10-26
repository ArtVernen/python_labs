
import csv
import json
from pathlib import Path

from src.lib.io_helpers import read_text, write_csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    """Преобразует JSON со списком словарей в CSV."""
    json_file = Path(json_path)
    csv_file = Path(csv_path)

    if json_file.suffix.lower() != ".json" or csv_file.suffix.lower() != ".csv":
        raise ValueError("Неверное расширение файла")

    if not json_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {json_path}")

    text = read_text(json_file)

    if not text.strip():
        raise ValueError("Пустой JSON")

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        raise ValueError("Некорректный JSON")

    if not isinstance(data, list) or not data:
        raise ValueError("Ожидается непустой список словарей")

    columns = []

    for item in data:
        if not isinstance(item, dict):
            raise ValueError("Ожидается список словарей")

        for key in item:
            if key not in columns:
                columns.append(key)

    if not columns:
        raise ValueError("JSON не содержит полей")

    rows = []

    for item in data:
        row = []

        for column in columns:
            row.append(item.get(column, ""))

        rows.append(row)

    write_csv(rows, csv_file, tuple(columns))


def csv_to_json(csv_path: str, json_path: str) -> None:
    """Преобразует CSV в JSON, сохраняя значения строками."""
    csv_file = Path(csv_path)
    json_file = Path(json_path)

    if csv_file.suffix.lower() != ".csv" or json_file.suffix.lower() != ".json":
        raise ValueError("Неверное расширение файла")

    if not csv_file.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")

    with csv_file.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        if not reader.fieldnames or "" in reader.fieldnames:
            raise ValueError("В CSV нет заголовка")

        if len(set(reader.fieldnames)) != len(reader.fieldnames):
            raise ValueError("Заголовки CSV повторяются")

        data = list(reader)

    if not data:
        raise ValueError("Пустой CSV или только заголовок")

    for row in data:
        if None in row:
            raise ValueError("В строке больше значений, чем заголовков")

        for key in row:
            if row[key] is None:
                row[key] = ""

    json_file.parent.mkdir(parents=True, exist_ok=True)

    with json_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    print("JSON -> CSV: готово")

    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
    print("CSV -> JSON: готово")
