n = int(input("Введите количество элементов последовательности: "))
x = 1
s = 0
print(x)
for i in range(n) :
    s +=x
    x/=2
    print(x)
print("Сумма ряда: ", s)