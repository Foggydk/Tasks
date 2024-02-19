x = int(input("Введите место"))
if x % 2 == 0 and x >= 1 and x <= 40:
    print("Купе верхнее")
elif x % 2 == 1 and x >= 1 and x <= 40:
    print("Купе нижнее")
elif x % 2 == 0 and x >= 41 and x <= 100:
    print("боковое верхнее")
elif x % 2 == 0 and x >= 41 and x <= 100:
    print("Боковое нижнее")
else:
    print('Неверно указано место')