# # Циклы
# #
# a = [1, 2, 3, 4, 5]
# for elements in a: # итерация по элементам
#     print(elements)
#
# for i in range(len(a)): # итерация по индексам
#     print(a[i])
#
# n = 10
# while n >= 0:
#     if n % 2 == 0:
#         print("Odd")
#     else:
#         print("Even")
#     n -= 1
#
# #Задачи
# n = int(input('Введите число: '))
# m = 1
# f = 1
# if n != 0:
#     while m <= n:
#         f = f * m
#         print(f'Factorial {m} = {f}')
#         m += 1
# else:
#     print('Factorial 0 = 1')
a1 = 0
a2 = 1
count = 2
target = int(input())
while target > a2:
    a2 = a1 + a2
    a1 = a2 - a1
    print(a2)
    if a2 == target:
        print('Bingo')
    elif a2 > target:
        print(-1)
    count += 1
print(count)

