from traceback import print_tb


n = int(input("Введите целое число не меньше 2\n"))
i = 2
while n%i !=0:
    i +=1
print("Наименьший натуральный делитель: ", i)