from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

def book_seat(event=None):
    s = seat_entry.get()
    try:
        if seats[s] == "свободно":
            seats[s] = "забронировано"
            update_canvas()
            mb.showinfo("Успех", f"Место {s} успешно забронировано.")
        else:
            mb.showerror("Ошибка", f"Место {s} уже забронировано.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {s} не существует.")

def cancel_booking(event=None):
    s = cancel_seat_entry.get()
    try:
        if seats[s] == "забронировано":
            seats[s] = "свободно"
            update_canvas()
            mb.showinfo("Успех", f"Бронь на месте {s} успешно отменена.")
        else:
            mb.showerror("Ошибка", f"Место {s} не забронировано или не существует.")
    except KeyError:
        mb.showerror("Ошибка", f"Место {s} не существует.")

def update_canvas():
    canvas.delete("all")
    for i, (seat, status) in enumerate(seats.items()):
        x = i * 40 + 20
        y = 20
        color = "green" if status == "свободно" else "red"
        canvas.create_rectangle(x, y, x+30, y+30, fill=color)
        canvas.create_text(x+15, y+15, text=seat)

window = Tk()
window.title("Бронирование мест")
window.geometry("400x300")

canvas = Canvas(width=400, height=60)
canvas.pack(pady=10)

seats = {f"Б{i}": "свободно" for i in range(1, 10)}
update_canvas()

# Контейнер (без expand и fill, чтобы не занимал всё окно)
container = ttk.Frame(window)
container.pack(pady=10)  # можно добавить отступ сверху/снизу

# Внутренний фрейм для элементов в ряд
row = ttk.Frame(container)
row.pack(anchor="center")  # выравнивание содержимого по центру

# Красный квадрат (Canvas даёт точную ширину/высоту в пикселях)
canvas_red = Canvas(row, width=30, height=30, highlightthickness=0)
canvas_red.create_rectangle(0, 0, 29, 29, fill="green", outline="black")
canvas_red.pack(side="left", padx=(0, 6))

# Надпись "свободно"
lbl_free = ttk.Label(row, text="свободно")
lbl_free.pack(side="left", padx=(0, 12))

# Зелёный квадрат
canvas_green = Canvas(row, width=30, height=30, highlightthickness=0)
canvas_green.create_rectangle(0, 0, 29, 29, fill="red", outline="black")
canvas_green.pack(side="left", padx=(0, 6))

# Надпись "забронировано"
lbl_reserved = ttk.Label(row, text="забронировано")
lbl_reserved.pack(side="left")

seat_entry = Entry()
seat_entry.pack(pady=5)
seat_entry.focus()
seat_entry.bind("<Return>", book_seat)
Button(text="Забронировать место", command=book_seat).pack(pady=5)

# Добавление поля ввода и кнопки для отмены бронирования
cancel_seat_entry = Entry()
cancel_seat_entry.pack(pady=5)
cancel_seat_entry.bind("<Return>", cancel_booking)

Button(text="Отменить бронь", command=cancel_booking).pack(pady=5)

window.mainloop()