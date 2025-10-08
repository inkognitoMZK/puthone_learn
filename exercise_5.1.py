import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Ввод ФИО — три фрейма")
root.geometry("400x300")

container = ttk.Frame(root, padding=12)
container.pack(fill="both", expand=True)

# Первый фрейм: имя
frame_name = ttk.LabelFrame(container, text="Имя", padding=10)
frame_name.pack(fill="x", pady=6)

lbl_name = ttk.Label(frame_name, text="Введите имя:")
lbl_name.grid(row=0, column=0, sticky="w")

entry_name = ttk.Entry(frame_name)
entry_name.grid(row=0, column=1, padx=8, sticky="ew")

frame_name.columnconfigure(1, weight=1)

# Второй фрейм: фамилия
frame_surname = ttk.LabelFrame(container, text="Фамилия", padding=10)
frame_surname.pack(fill="x", pady=6)

lbl_surname = ttk.Label(frame_surname, text="Введите фамилию:")
lbl_surname.grid(row=0, column=0, sticky="w")

entry_surname = ttk.Entry(frame_surname)
entry_surname.grid(row=0, column=1, padx=8, sticky="ew")

frame_surname.columnconfigure(1, weight=1)

# Третий фрейм: отчество
frame_patronymic = ttk.LabelFrame(container, text="Отчество", padding=10)
frame_patronymic.pack(fill="x", pady=6)

lbl_patronymic = ttk.Label(frame_patronymic, text="Введите отчество:")
lbl_patronymic.grid(row=0, column=0, sticky="w")

entry_patronymic = ttk.Entry(frame_patronymic)
entry_patronymic.grid(row=0, column=1, padx=8, sticky="ew")

frame_patronymic.columnconfigure(1, weight=1)

root.mainloop()
