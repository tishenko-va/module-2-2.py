first = int(input('Умножте 2 на 3:'))
second = int(input('Умножте 2 на 4:'))
third = int(input('Умножте 2 на 5:'))
if first == second and second==third and third==first:
    print(3)
elif first == second or second==third or third==first:
    print(2)
else:
    print(0)
    