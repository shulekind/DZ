a = int(input("Введите чиcло "))
count = 0
for i in range(a):
    num = int(input("Введите чиcло "))
    if num == 0:
        count += 1
        print("Количество раз ты ввел ноль: ",count)