import os
import shutil
import tkinter as tk
from tkinter import filedialog

def main():
    # Скрываем основное окно
    root = tk.Tk()
    root.withdraw()

    # Диалог выбора папки
    folder_selected = filedialog.askdirectory(title="Выберите папку с файлами .doc и .docx")

    if not folder_selected:
        print("Папка не выбрана. Программа завершена.")
        return

    # Создаём новую папку с суффиксом "_new"
    new_folder = folder_selected + "_new"
    os.makedirs(new_folder, exist_ok=True)

    # Перебираем файлы в выбранной папке
    for filename in os.listdir(folder_selected):
        if filename.lower().endswith(('.doc', '.docx')):
            old_path = os.path.join(folder_selected, filename)
            new_path = os.path.join(new_folder, filename)
            shutil.move(old_path, new_path)
            print(f"Файл перемещён: {filename}")

    print(f"\nВсе файлы .doc и .docx перемещены в папку:\n{new_folder}")
    input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    main()
