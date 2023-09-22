from Creation import Creation
from Saving import Saving
from Reading import read_all_notes
from Editing import editing_note
from Delete import del_note
from Download import download_notes
from Sorting import sort_note

def user_interface():
    info = "Данная программа позволяет создавать, редактировать и просматривать заметки.\n" \
           "Команды используемые для работы с программой: \n" \
           "1 - справка по работе программы;\n" \
           "2  - создание заметки;\n" \
           "3 - просмотр заметок;\n" \
           "4 - изменение заметок;\n" \
           "Q - выход из программы;\n" \
           "5 - удалить заметку;\n" \
           "6 - выгрузить в файл JSON\n" \
           "7 - сортировка по дате создания заметки по возрастанию\n" \
           "8 - сортировка по дате создания заметки по убыванию\n"
    while True:
        print("Введите команду: (1 - Help)")
        user_input = input().lower()
        if user_input == "2":
            title = input("Введите название заметки: ")
            text = input("Введите содержание заметки: ")
            note = Creation(title, text)
            save = Saving(note.note())
            save.saving_note()
        elif user_input == "4":
            editing_note("note.json")
        elif user_input == "3":
            read_all_notes("note.json")
        elif user_input == "1":
            print(info)
        elif user_input == "5":
            save = Saving(del_note("note.json"))
            save.saving_note()
        elif user_input == "q" or "Q":
            break
        elif user_input == "6":
            download_notes("note.json")
        elif user_input == "7":
            sort_note("note.json", order=True)
            print("Заметки отсортированы по возрастанию")
        elif user_input == "8":
            sort_note("note.json", order=False)
            print("Заметки отсортированы по убыванию")
        else:
            print("Команда не найдена. help - справка о работе программы")