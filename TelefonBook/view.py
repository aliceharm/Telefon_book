import funk as f


def menu():
    print('Здравствуйте!\n Вас приветствует самая лучшая телефонная книга')
    variant = input('Вы можете: \n Добавить контакт - нажмите 1;\
         \n Удалить контакт - нажмите 2;\
         \n Исправить контакт - нажмите 3;\
          \n Поиск заветного контакта - нажмите 4;\
           \n Импорт телефонной книги из файла - нажмите 5;\
            \n Введите пункт меню -')
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
    data = f.export_data()
    item = f.search_data(word, data)
    if item != None:
        print("Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        print(item)
    else:
        print("Данные не обнаружены")
