#`python
from fntgai import getcontent
def read_table_of_contents(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    content = ""
    book_title = None
    subpoint = ""
    current_chapter = None
    counter=0
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
        content = content + getcontent(f"Напиши подпункт {subpoint} {current_chapter} книги {book_title}")+ "\n"
        counter=counter+1
        print(str(counter)+" "+subpoint)
    file_name = "output.txt"

# Открываем файл в режиме записи ('w')
    with open(file_name, 'w', encoding='utf-8') as file:
# Записываем содержимое переменной в файл
        file.write(content)
        print("содержание готово")

# Путь к файлу с оглавлением
file_path = 'pop.txt'

# Чтение и вывод оглавления
#print("hello")
read_table_of_contents(file_path)
