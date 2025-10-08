def temperature():

  t = input("Введите температуру воды: ")

  if t.isdigit():

    t = int(t)

    if t <= 0:
      print("Озеро замерзло")

    elif  t > 0  and  t < 10:
      print("Ледяная вода")

    elif t >= 10  and  t < 15:
      print("Жуть как холодно") 

    elif t >= 15  and  t < 18:
      print("Прохладно, но можно искупаться")

    elif t >= 18  and  t < 24:
      print("Кайф") 

    elif t >= 24  and  t < 30:
      print("Полный кайф") 

    elif t >= 30  and  t < 36:
      print("Горячая") 

    else: 
      print("Кипяток")
  else:
    print("Введено не число")
    temperature()

temperature()
