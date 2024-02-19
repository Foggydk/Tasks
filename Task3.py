def f(y):
    if y % 4 == 0 and not(y % 100 == 0) or y % 400 == 0:
        return True
    else:
        return False


x = int(input("Введите год"))
if f(x) == True:
    print("Год високосный")
else:
    print('Год не високосный')