
# Лабораторная работа №6

**Хохлов Никита, БИВТ-26-6-1**

## 1. Работа с текстом — cli_text.py

В этом файле сделаны две команды: `cat` и `stats`. Для работы с аргументами используется `argparse`.

### Команда cat

Выводит содержимое файла в терминал. С помощью флага `-n` можно включить нумерацию строк.

**Тест 1. Вывод файла без нумерации**

```bash
python -m src.lab06.cli_text cat --input data/samples/people.csv
```

![cat без нумерации](../../images/lab06/cat_without_numbers.png)

**Тест 2. Вывод файла с нумерацией**

```bash
python -m src.lab06.cli_text cat --input data/samples/people.csv -n
```

![cat с нумерацией](../../images/lab06/cat_with_numbers.png)

### Команда stats

Считает общее количество слов, количество уникальных слов и выводит самые частые слова. Используются функции из третьей лабораторной.

**Тест 3. Статистика с top по умолчанию**

По умолчанию выводится 5 самых частых слов.

```bash
python -m src.lab06.cli_text stats --input data/samples/lab06_words.txt
```

![Статистика top 5](../../images/lab06/stats_top5.png)

**Тест 4. Статистика с top 3**

```bash
python -m src.lab06.cli_text stats --input data/samples/lab06_words.txt --top 3
```

![Статистика top 3](../../images/lab06/stats_top3.png)

### Проверка ошибок cli_text

**Тест 5. Несуществующий файл**

Проверяем, как программа реагирует на отсутствие файла.

```bash
python -m src.lab06.cli_text cat --input data/samples/missing.txt
```

![Ошибка отсутствующего файла](../../images/lab06/cli_text_missing.png)

**Тест 6. Отрицательное значение top**

Значение `--top` должно быть больше нуля.

```bash
python -m src.lab06.cli_text stats --input data/samples/lab06_words.txt --top -3
```

![Ошибка top](../../images/lab06/cli_text_top_error.png)

### Проверка справки cli_text

**Тест 7. Общая справка**

```bash
python -m src.lab06.cli_text --help
```

![Справка cli_text](../../images/lab06/cli_text_help.png)

**Тест 8. Справка cat**

```bash
python -m src.lab06.cli_text cat --help
```

![Справка cat](../../images/lab06/cli_text_cat_help.png)

**Тест 9. Справка stats**

```bash
python -m src.lab06.cli_text stats --help
```

![Справка stats](../../images/lab06/cli_text_stats_help.png)

---

## 2. Конвертация файлов — cli_convert.py

Здесь реализованы три команды: `json2csv`, `csv2json` и `csv2xlsx`.

Для конвертации используются функции из пятой лабораторной.

Аргумент `--in` указывает исходный файл, а `--out` — путь для сохранения результата.

### Проверка конвертации

**Тест 10. JSON в CSV**

```bash
python -m src.lab06.cli_convert json2csv --in data/samples/people.json --out data/out/people_from_json.csv
```

![JSON в CSV](../../images/lab06/json2csv.png)

**Тест 11. CSV в JSON**

```bash
python -m src.lab06.cli_convert csv2json --in data/samples/people.csv --out data/out/people_from_csv.json
```

![CSV в JSON](../../images/lab06/csv2json.png)

**Тест 12. CSV в XLSX**

```bash
python -m src.lab06.cli_convert csv2xlsx --in data/samples/people.csv --out data/out/people.xlsx
```

![CSV в XLSX](../../images/lab06/csv2xlsx.png)

### Проверка ошибок cli_convert

**Тест 13. Запуск без обязательных аргументов**

Проверяем, что программа сообщает об отсутствии `--in` и `--out`.

```bash
python -m src.lab06.cli_convert json2csv
```

![Ошибка аргументов](../../images/lab06/cli_convert_value_error.png)

### Проверка справки cli_convert

**Тест 14. Общая справка**

```bash
python -m src.lab06.cli_convert --help
```

![Справка cli_convert](../../images/lab06/cli_convert_help.png)

**Тест 15. Справка json2csv**

```bash
python -m src.lab06.cli_convert json2csv --help
```

![Справка json2csv](../../images/lab06/cli_convert_json2csv_help.png)

**Тест 16. Справка csv2json**

```bash
python -m src.lab06.cli_convert csv2json --help
```

![Справка csv2json](../../images/lab06/cli_convert_csv2json_help.png)

**Тест 17. Справка csv2xlsx**

```bash
python -m src.lab06.cli_convert csv2xlsx --help
```

![Справка csv2xlsx](../../images/lab06/cli_convert_csv2xlsx_help.png)
