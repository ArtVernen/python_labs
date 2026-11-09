
import argparse

from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(description="Конвертер файлов")
    subparsers = parser.add_subparsers(dest="command", required=True)

    json2csv = subparsers.add_parser("json2csv")
    json2csv.add_argument("--in", dest="input", required=True)
    json2csv.add_argument("--out", dest="output", required=True)

    csv2json = subparsers.add_parser("csv2json")
    csv2json.add_argument("--in", dest="input", required=True)
    csv2json.add_argument("--out", dest="output", required=True)

    csv2xlsx = subparsers.add_parser("csv2xlsx")
    csv2xlsx.add_argument("--in", dest="input", required=True)
    csv2xlsx.add_argument("--out", dest="output", required=True)

    args = parser.parse_args()

    try:
        if args.command == "json2csv":
            json_to_csv(args.input, args.output)
        elif args.command == "csv2json":
            csv_to_json(args.input, args.output)
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input, args.output)

        print("Конвертация выполнена")

    except FileNotFoundError:
        parser.error("Файл не найден")
    except UnicodeDecodeError:
        parser.error("Неверная кодировка файла")
    except ValueError as error:
        parser.error(str(error))


if __name__ == "__main__":
    main()
