# Урок 1. Ввод-Вывод, операторы ветвления
# Задача 2: Найдите сумму цифр трехзначного числа.

var = input("Input number: ")
summ = 0
for i in range(len(var)):
    temp = (var[i])
    summ += int(temp)
print(f'Сумма чисел: {var} = {summ}')

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали
# одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Введите кол-во журавликов : "))
petya = s / 6
serega = petya
katya = (petya + serega) * 2
print(f'Катя = {katya}, Петя = {petya}, Сережа = {serega}')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд
# и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

def summa(num):
    summ = int(num[0]) + int(num[1]) + int(num[2])
    return summ


number = int(input("Введите номер билета : "))
number1 = str(number // 1000)
number2 = str(number % 1000)
sum1 = summa(number1)
sum2 = summa(number2)
if summa(number1) == summa(number2):
    print(f'{sum1} = {sum2}, Счастливый билет!')
else:
    print('Не повезло!')

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n, m = input("Введите размер шоколадки N на M : ").split()
k = input("Введите кол-во долек: ")
print(n, m, k)
if int(k) % int(n) == 0 or int(k) % int(m) == 0:
    print("Yes")
else:
    print('No')