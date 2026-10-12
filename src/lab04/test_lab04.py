
import csv
import io
import sys
import tempfile
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]

sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "src" / "lab04"))

from io_txt_csv import read_text, ensure_parent_dir, write_csv
import text_report


def check(label, actual, expected):
    assert actual == expected, f"{label}: ожидалось {expected!r}, получено {actual!r}"
    print(f"{label} -> {actual!r}")


def check_error(label, error_type, function):
    try:
        function()
    except error_type:
        print(f"{label} -> {error_type.__name__}")
    else:
        raise AssertionError(f"{label}: ожидалась ошибка {error_type.__name__}")


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.reader(file))


def run_report(folder, star=False, table=False, encoding="utf-8"):
    data = folder / "data"
    output = io.StringIO()

    with patch.object(text_report, "ROOT", folder), \
         patch.object(text_report, "INPUT_FILE", data / "input.txt"), \
         patch.object(text_report, "STAR_FILES", [data / "a.txt", data / "b.txt"]), \
         patch.object(text_report, "STAR_MODE", star), \
         patch.object(text_report, "TABLE_MODE", table), \
         patch.object(text_report, "ENCODING", encoding), \
         redirect_stdout(output):

        text_report.main()

    return output.getvalue()


def main():
    with tempfile.TemporaryDirectory() as temporary:
        folder = Path(temporary)
        data = folder / "data"
        data.mkdir()

        print("=== read_text ===")

        txt = data / "input.txt"
        txt.write_text("Привет, мир!", encoding="utf-8")
        check("UTF-8", read_text(txt), "Привет, мир!")

        txt.write_text("", encoding="utf-8")
        check("Пустой файл", read_text(txt), "")

        cp_file = data / "windows.txt"
        cp_file.write_text("Привет", encoding="cp1251")
        check("CP1251", read_text(cp_file, encoding="cp1251"), "Привет")

        check_error(
            "Нет файла",
            FileNotFoundError,
            lambda: read_text(data / "missing.txt")
        )

        check_error(
            "Неверная кодировка",
            UnicodeDecodeError,
            lambda: read_text(cp_file, encoding="utf-8")
        )

        print("\n=== ensure_parent_dir ★ ===")

        nested = data / "reports" / "2026" / "report.csv"
        ensure_parent_dir(nested)
        check("Создание папок", nested.parent.is_dir(), True)

        ensure_parent_dir(nested)
        check("Повторный вызов", nested.parent.is_dir(), True)

        print("\n=== write_csv ===")

        csv_path = data / "example.csv"

        write_csv(
            [("кот", 3), ("пёс", 2)],
            csv_path,
            header=("word", "count")
        )

        check(
            "CSV с заголовком",
            read_csv(csv_path),
            [["word", "count"], ["кот", "3"], ["пёс", "2"]]
        )

        write_csv([("кот", 3)], csv_path)
        check("Без заголовка", read_csv(csv_path), [["кот", "3"]])

        write_csv([], csv_path, header=("word", "count"))
        check("Без данных", read_csv(csv_path), [["word", "count"]])

        write_csv([("новое", 1)], csv_path)
        check("Перезапись", read_csv(csv_path), [["новое", "1"]])

        check_error(
            "Разное число столбцов",
            ValueError,
            lambda: write_csv([("кот", 1), ("пёс", 2, 3)], csv_path)
        )

        print("\n=== text_report.py ===")

        txt.write_text("Привет, мир! Привет!!!", encoding="utf-8")

        result = run_report(folder)
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

        check(
            "report.csv",
            read_csv(data / "report.csv"),
            [["word", "count"], ["привет", "2"], ["мир", "1"]]
        )

        print("\n=== Пустой TXT ===")

        txt.write_text("", encoding="utf-8")

        result = run_report(folder)

        assert result == "Всего слов: 0\nУникальных слов: 0\nТоп-5:\n"
        print(result, end="")

        check(
            "report.csv",
            read_csv(data / "report.csv"),
            [["word", "count"]]
        )

        print("\n=== Отчёт в CP1251 ===")

        txt.write_text("Привет", encoding="cp1251")

        result = run_report(folder, encoding="cp1251")
        print(result, end="")

        check(
            "report.csv",
            read_csv(data / "report.csv"),
            [["word", "count"], ["привет", "1"]]
        )

        print("\n=== Несколько файлов ★ ===")

        (data / "a.txt").write_text("Привет мир", encoding="utf-8")
        (data / "b.txt").write_text("Привет, привет!", encoding="utf-8")

        result = run_report(folder, star=True)

        assert "Всего слов: 4" in result
        print(result, end="")

        check(
            "report_per_file.csv",
            read_csv(data / "report_per_file.csv"),
            [
                ["file", "word", "count"],
                ["a.txt", "мир", "1"],
                ["a.txt", "привет", "1"],
                ["b.txt", "привет", "2"]
            ]
        )

        check(
            "report_total.csv",
            read_csv(data / "report_total.csv"),
            [
                ["word", "count"],
                ["привет", "3"],
                ["мир", "1"]
            ]
        )

        print("\n=== Таблица ★ ===")

        result = run_report(folder, star=True, table=True)

        assert "привет | 3" in result
        assert "частота" in result

        print(result, end="")


if __name__ == "__main__":
    main()
