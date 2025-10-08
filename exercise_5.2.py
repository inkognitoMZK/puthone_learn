import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


def safe_get(entry):
    """Получает число из поля или возвращает 0, если поле пустое.
    Поддерживает дробные числа с запятой.
    """
    text = entry.get().strip()
    if text == "":
        return 0
    # заменяем запятую на точку
    text = text.replace(",", ".")
    return float(text)


def calculate_sum(entries):
    try:
        values = [safe_get(e) for e in entries]
        result = sum(values)
        messagebox.showinfo("Результат", f"Сумма: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")


def calculate_product(entries):
    try:
        values = [safe_get(e) for e in entries]
        result = 1
        for v in values:
            result *= v
        messagebox.showinfo("Результат", f"Произведение: {result}")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректные числа!")

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x250")
root.resizable(True, True)

container = ttk.Frame(root, padding=12)
container.pack(fill="both", expand=True)

label_info = ttk.Label(container, text="Введите три числа и нажмите на кнопку для вычисления суммы")
label_info.pack(pady=8)

entries = []
for i in range(3):
    entry = ttk.Entry(container)
    entry.pack(pady=4, fill="x")
    entries.append(entry)

btn_sum = ttk.Button(container, text="Сложить три числа", command=lambda: calculate_sum(entries))
btn_sum.pack(pady=6, fill="x")

btn_product = ttk.Button(container, text="Умножить три числа", command=lambda: calculate_product(entries))
btn_product.pack(pady=6, fill="x")

root.mainloop()
