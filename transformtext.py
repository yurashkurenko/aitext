def process_file(input_file, output_file, transform_function):
    """
    Считывает текст из входного файла, применяет функцию преобразования и сохраняет результат в выходной файл.

    Аргументы:
        input_file (str): Путь к входному файлу.
        output_file (str): Путь к выходному файлу.
        transform_function (function): Функция, которая принимает строку в качестве входных данных и возвращает преобразованную строку.
    """

    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                transformed_line = transform_function(line)
                outfile.write(transformed_line)

        print(f"Файл успешно обработан. Результат сохранен в {output_file}")

    except FileNotFoundError:
        print(f"Ошибка: файл '{input_file}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример функции преобразования (преобразование текста в верхний регистр)
def to_uppercase(text):
    return text.upper()

# Пример использования
if __name__ == "__main__":
    input_filename = 'input.txt'  # Замените на имя вашего входного файла
    output_filename = 'output.txt' # Замените на имя вашего выходного файла

    # Вызов функции process_file с функцией преобразования в верхний регистр
    process_file(input_filename, output_filename, to_uppercase)