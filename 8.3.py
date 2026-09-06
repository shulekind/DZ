m = int(input("Максимальная масса, которую может выдержать баркас: "))
n = int(input("Колличество рыбаков стоящих на берегу реки: "))
mass = []
for i in range(n) :
    i = int(input("Введите массу рыбака: "))
    if m > i:
        mass.append(i)
else:
    print("Извини друг, лодка с тобой потонет")
mass.sort()
left = 0
right = len(mass) - 1
boat = 0
while left <= right:
    if mass[left] + mass[right] <= m:
        left +=1
        right -= 1
        boat += 1
print(f'Колличетво лодок которые понадобятся: {boat}')