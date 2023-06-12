#~/Users/station/Desktop/HomeWork/
# import os
# a = 'abcdf'
# with open('/Users/station/PycharmProjects/HomeWorkPython/file.txt', 'r+') as f:
#     # f.write(' Hey there ')
#     # text = f.readlines()
#     # if 'Hello world' not in text:
#     #     f.write('Hello world')
#     # f.writelines([])
#     text = f.readlines()
#
# print(text)
# t = text.copy()
# tt = t.reverse()
# print(t, tt)

# Задача №49. Общее обсуждение Создать телефонный справочник с возможностью импорта и экспорта
# данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1.Программа должна выводить данные
# 2.Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека) 4.Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

def update(data):
    with open('/Users/station/PycharmProjects/HomeWorkPython/file.txt', 'w+') as newfile:
        newfile.writelines(data)


with open('/Users/station/PycharmProjects/HomeWorkPython/file.txt', 'r+') as file:
    file = file.readlines()
print(file)
while True:
    option = int(input('Выберите действие:\n1 - поиск 2 - редактирование пользователя 3 - добавление пользователя 4 - удаление пользователя\n: '))
    if option == 1:
        search = input('Для поиска введите Фамилию (Имя), телефон: ')
        for i in file:
            if search in i:
                print(i)
    elif option == 2:
        search = input('Для редактирования введите Фамилию (Имя), телефон: ')
        for i in range(len(file)):
            if search in file[i]:
                print(file[i])
                option2 = str(input('Редактировать? Y/N: '))
                if option2 == 'Y':
                    file.remove(file[i])
                    add = input('Для редактирования введите Фамилию,Имя, Отчество, телефон пользователя: ')
                    file.insert(i, add + '\n')
                    update(file)
    elif option == 3:
        add = input('Для добавления введите Фамилию,Имя, Отчество, телефон пользователя: ')
        file.append(add + '\n')
        print(file)
        update(file)
    elif option == 4:
        search = input('Для удаления введите Фамилию (Имя), телефон: ')
        for i in range(len(file)):
            if search in file[i]:
                print(file[i])
                option2 = str(input('Удалить? Y/N: '))
                if option2 == 'Y':
                    file.remove(file[i])
                    update(file)
                    break




