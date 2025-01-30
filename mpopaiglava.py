#`python

def read_table_of_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    content = ""
    book_title = None
    current_chapter = None

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # Определяем название книги
        if book_title is None:
            book_title = line
            continue

        # Определяем название главы
        if line.startswith("Глава"):
            current_chapter = line
            continue

        # Определяем подпункт
        if line[0].isdigit() and '.' in line:
            subpoint = line
#            print(f"Книга: {book_title}, Глава: {current_chapter}, Подпункт: {subpoint}")
#            print(f"Напиши подпункт {subpoint} {current_chapter} книги {book_title}")
        content = content + (f"Напиши подпункт {subpoint} {current_chapter} книги {book_title}")+ "\n"
    print(content)

# Путь к файлу с оглавлением
file_path = 'pop.txt'

# Чтение и вывод оглавления
print("hello")
read_table_of_contents(file_path)
