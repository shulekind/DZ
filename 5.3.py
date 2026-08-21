summa = int(input("Минимальная сумма инвестиций - "))
Maikl = int(input("Cколько долларов у Майкла - "))
ivan = int(input("Сколько долларов у Ивана - "))
if (Maikl >= summa) and (ivan >= summa):
 print(2)
elif (Maikl >= summa) and (ivan <= summa):
 print("Maikl")
elif (Maikl <= summa) and (ivan >= summa):
 print("Ivan")
elif (Maikl <= summa) and (ivan <= summa) and ((Maikl + ivan) >= summa):
 print(1)
elif (Maikl <= summa) and (ivan <= summa) and ((Maikl + ivan) <= summa):
 print(0)