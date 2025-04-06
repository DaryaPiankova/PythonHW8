"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. 
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных 
файлов и директорий.
"""

import os

def rename_files(target_name, num_digits, original_ext, final_ext, name_range):
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith(original_ext)]
    for index, file in enumerate(files):
        base_name = os.path.splitext(file)[0]
        start, end = name_range
        extracted_part = base_name[start:end]
        new_file_name = f"{extracted_part}{target_name}{str(index + 1).zfill(num_digits)}.{final_ext}"
        os.rename(file, new_file_name)
        print(f"Переименован: {file} -> {new_file_name}")


rename_files(target_name='new_file', num_digits=3, original_ext='.txt', final_ext='txt', name_range=(3, 6))
