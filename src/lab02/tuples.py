def format_record(rec: tuple[str, str, float]) -> str:
    """Форматирует запись о студенте."""
    if type(rec) != tuple:
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("В записи должно быть 3 элемента")
    
    fio, group, gpa = rec

    if type(fio) != str or type(group) != str:
        raise TypeError("ФИО и группа должны быть строками")
    if type(gpa) != int and type(gpa) != float:
        raise TypeError("GPA должен быть числом")
    
    parts = fio.split()
    group = group.strip()

    if len(parts) < 2:
        raise ValueError("Неверное ФИО")
    if group == "":
        raise ValueError("Группа пустая")
    if gpa < 0 or gpa > 5:
        raise ValueError("GPA должен быть от 0 до 5")
    
    surname = parts[0].capitalize()
    initials = ""
    for i in range(1, len(parts)):
        if i > 2:
            break
        initials += parts[i][0].upper() + "."
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"

#тест кейс
if __name__ == "__main__":
    print("format_record")
    print(f'("Иванов Иван Иванович", "BIVT-25", 4.6) → "{format_record(("Иванов Иван Иванович", "BIVT-25", 4.6))}"')
    print(f'("Петров Пётр", "IKBO-12", 5.0) → "{format_record(("Петров Пётр", "IKBO-12", 5.0))}"')
    print(f'("Петров Пётр Петрович", "IKBO-12", 5.0) → "{format_record(("Петров Пётр Петрович", "IKBO-12", 5.0))}"')
    print(f'("  сидорова  анна   сергеевна ", "ABB-01", 3.999) → "{format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))}"')
    print(format_record(("", "BIVT-25", 4.5)))