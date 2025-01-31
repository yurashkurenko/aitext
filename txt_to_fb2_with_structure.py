import os
import sys
import uuid
from datetime import datetime
import xml.etree.ElementTree as ET
import argparse
import re

# Используем пространство имен FB2
FB2_NS = "http://www.gribuser.ru/xml/fictionbook/2.0"
ET.register_namespace('', FB2_NS)

def generate_fb2(text_content, title="Без названия", author="Неизвестный"):
    # Создаем корневой элемент
    fictionbook = ET.Element('{%s}FictionBook' % FB2_NS)
    
    # Описательная часть
    description = ET.SubElement(fictionbook, 'description')

    # Титульная информация
    title_info = ET.SubElement(description, 'title-info')
    ET.SubElement(title_info, 'genre').text = 'unknown'
    authors = create_author_elements(author)
    for auth in authors:
        title_info.append(auth)
    ET.SubElement(title_info, 'book-title').text = title
    ET.SubElement(title_info, 'date').text = datetime.now().strftime("%Y-%m-%d")

    # Информационный раздел
    document_info = ET.SubElement(description, 'document-info')
    for auth in authors:
        document_info.append(auth)
    ET.SubElement(document_info, 'program-used').text = 'txt_to_fb2_with_structure.py'

    # Содержательная часть
    body = ET.SubElement(fictionbook, 'body')

    # Разбор текста на линии
    lines = text_content.split('\n')
    current_section = body  # Начинаем с корневого тела книги
    section_stack = []  # Стек для хранения текущих разделов

    for line in lines:
        line = line.strip()
        if not line:
            continue  # Пропускаем пустые строки

        # Определяем уровень структуры
        chapter_match = re.match(r'^(Глава|ГЛАВА)\s+\d+\.?\s*(.*)', line)
        heading_match = re.match(r'^#{1}\s+(.*)', line)
        subheading_match = re.match(r'^#{2}\s+(.*)', line)

        if chapter_match:
            # Создаем новый раздел для главы
            chapter_title = chapter_match.group(0)
            section = ET.SubElement(body, 'section')
            title_element = ET.SubElement(section, 'title')
            p = ET.SubElement(title_element, 'p')
            p.text = chapter_title
            current_section = section
            section_stack = [section]  # Сброс стека
        elif heading_match:
            # Создаем подраздел для заголовка
            heading_title = heading_match.group(1).strip()
            section = ET.SubElement(current_section, 'section')
            title_element = ET.SubElement(section, 'title')
            p = ET.SubElement(title_element, 'p')
            p.text = heading_title
            section_stack.append(section)
            current_section = section
        elif subheading_match:
            # Создаем подраздел для подзаголовка
            subheading_title = subheading_match.group(1).strip()
            section = ET.SubElement(current_section, 'section')
            title_element = ET.SubElement(section, 'title')
            p = ET.SubElement(title_element, 'p')
            p.text = subheading_title
            section_stack.append(section)
            current_section = section
        else:
            # Обычный абзац
            p = ET.SubElement(current_section, 'p')
            p.text = line

    return fictionbook

def create_author_elements(author_str):
    authors = []
    # Предполагаем, что авторы разделены запятой
    author_list = [a.strip() for a in author_str.split(',')]
    for author in author_list:
        names = author.split()
        if len(names) == 1:
            author_elem = ET.Element('author')
            ET.SubElement(author_elem, 'last-name').text = names[0]
        elif len(names) >= 2:
            author_elem = ET.Element('author')
            ET.SubElement(author_elem, 'first-name').text = names[0]
            ET.SubElement(author_elem, 'last-name').text = ' '.join(names[1:])
        authors.append(author_elem)
    return authors

def save_fb2(fictionbook, output_path):
    tree = ET.ElementTree(fictionbook)
    tree.write(output_path, encoding='utf-8', xml_declaration=True)
    # Для более красивого форматирования можно использовать библиотеку lxml
    try:
        from lxml import etree
        parser = etree.XMLParser(remove_blank_text=True)
        tree = etree.parse(output_path, parser)
        tree.write(output_path, pretty_print=True, encoding='utf-8', xml_declaration=True)
    except ImportError:
        pass  # Если lxml не установлен, сохранение всё равно произойдет

def main(input_file, output_file, title, author):
    if not os.path.isfile(input_file):
        print(f"Файл {input_file} не найден.")
        sys.exit(1)

    with open(input_file, 'r', encoding='utf-8') as f:
        text_content = f.read()

    fb2_tree = generate_fb2(text_content, title, author)
    save_fb2(fb2_tree, output_file)
    print(f"FB2 файл успешно создан: {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Конвертировать TXT в FB2 с разметкой глав и заголовков.')
    parser.add_argument('input', help='Входной текстовый файл')
    parser.add_argument('output', help='Выходной FB2 файл')
    parser.add_argument('--title', default="Без названия", help='Название книги')
    parser.add_argument('--author', default="Неизвестный", help='Автор книги')

    args = parser.parse_args()
    main(args.input, args.output, args.title, args.author)