import funk as f


def menu():
    print('Здравствуйте!\nВас приветствует самая лучшая телефонная книга')
    list_ = ["1", "2", "3", "4", "0"]
    variant = input('Вы можете: \nДобавить контакт - нажмите 1;\
         \nУдалить контакт - нажмите 2;\
          \nПоиск заветного контакта - нажмите 3;\
           \nИмпорт телефонной книги из файла - нажмите 4;\
           \nВыйти из книги - 0;\
            \nВведите пункт меню - ')
    while variant not in list_:
        variant = input("Ведите правильное число: ")
    return variant


def print_adding_contact():
    surname = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    f.add_contact(surname, first_name, patronymic, phone_number)
    print("Контакт сохранен")


def print_search():
    word = input("Введите данные для поиска: ")
    data_list = f.export_data()
    item = f.search_data(word, data_list)[0]
    if item != ([], []):
        # print("Фамилия".center(20), "Имя".center(20),
        #       "Телефон".center(15), "Примечание".center(30))
        # print("-"*85)
        print(item)
    else:
        print("Данные не обнаружены")


def print_import_book(name_file):
    print(f"Контакты из файла {name_file} добавлены!")


def print_exit():
    print("До новых встреч!")


def print_del_cont():
    word = input("Введите данные для удаления контакта: ")
    data_list = f.export_data()
    del_ = f.search_data(word, data_list)[0]
    if del_ != []:
        if len(del_) == 2:
            return del_[1]
        else:
            print(
                "Найдено несколько контактов.")
            print(del_)
            index_del = int(
                input("Выберите номер удаляемого контакта, в соответсвии с пледложенными: "))
            while index_del not in f.search_data(word, data_list)[1]:
                index_del = int(input("Ведите правильное число: "))
            return index_del
    else:
        return print("Контакт не найден")


def print_del():
    print(f"Контакт удален")
