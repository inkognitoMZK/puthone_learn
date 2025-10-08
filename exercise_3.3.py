# 1 задание
n = 1

while n < 82:
    print(n)
    n = n + 20

# 2 задание

password = input("Введите пароль: ")

while len(password) < 8:
    print("Пароль слишком короткий! Минимальная длина — 8 символов.")
    password = input("Введите пароль: ")

print("Пароль принят!")