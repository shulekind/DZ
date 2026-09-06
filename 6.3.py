a = int( input("Число a: ") )
b = int( input("Число b: ") ) + 1
[ print(num, end = " ") for num in range(a,b) if a < b and num % 2 == 0]