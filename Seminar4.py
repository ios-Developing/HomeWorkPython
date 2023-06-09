# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

s = 'a a c c c c b a c b b d d d d d'.split()
for i, letter in enumerate(s):
    if s[:i].count(letter)<1:
        r += letter + ' '
    b = a.count()
print(b)

# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.

s = "She sells, sea shells on the sea shore. The shells\
 that she sells are sea shells! I'm sure So if she sells sea \
shells on the sea shore? I'm sure that\n the shells are sea \
shore shells"
r = [i.strip('.,?!\n').lower() for i in s.split()]
r = set(r)  # множество - уникальные значения
print(r)
print(len(r))


# Ваня и Петя поспорили, кто быстрее решит
# следующую задачу: “Задана последовательность
# неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента
# последовательности, которая завершается первым
# встретившимся нулем (число 0 не входит в
# последовательность)”. Однако 2 друга оказались не
# такими смышлеными. Никто из ребят не смог до
# конца сделать это задание. Они решили так: у кого
# будет меньше ошибок в коде, тот и выиграл спор. За
# помощью товарищи обратились к Вам, студентам.

num = int(input())
max = num
while num != 0:
    if num > max and num != 0:
       max = num
    num = int(input())
print(f'{max = }')

# s = 'a a c c c c b a c b b d d d d d'.split()
# l = {}
# r = ''
# for i in range(len(s)):
#     if s[i] not in l.keys():
#         l[s[i]] = 1
#         r += f'{s[i]} '
#     else:
#         r += f'{s[i]}_{l[s[i]]} '
#         l[s[i]] += 1
# print(r)
