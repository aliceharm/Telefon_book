import view as v


def import_book():
    name_ = input(
        'Введите имя файла, из которого импортируется телефонная книга - ')
    with open(f'{name_}.txt', 'r') as f:
        data_Book = f.read()

    with open('Telefon_Book.txt', 'a') as f:
        f.write(data_Book + '\n\n')
    v.print_import_book(name_)


def add_contact(surname, first_name, patronymic, phone_number):
    with open('Telefon_Book.txt', 'a', encoding='utf-8') as f:
        f.write(surname + '\n' + first_name + '\n' +
                patronymic + '\n' + phone_number + '\n\n')


def search_data(word, data_list):
    if len(data_list) > 0:
        resalt = []
        for item in data_list:
            if word in item:
                resalt.append(item)
        return resalt
    else:
        return None


def export_data():
    data_B = []
    with open('Telefon_Book.txt', 'r', encoding='utf-8') as file:
        data_B = file.read()
        list_cont = data_B.split("\n\n")
        # list_ = []
        # t = []
        # for line in data_B:
        #     if line != "":
        #         t.append(line)
        #     else:
        #         list_.append(t)
        #         t.clear
    return list_cont


# def del_contact():
#     list_ = export_data()
