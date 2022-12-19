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
    resalt = []
    count = 0
    list_count = []
    for item in data_list:
        if word in item:
            resalt.append(item)
            resalt.append(count)
            list_count.append(count)
        count += 1
    return resalt, list_count


def export_data():
    data_B = []
    with open('Telefon_Book.txt', 'r', encoding='utf-8') as file:
        data_B = file.read()
        list_cont = data_B.split("\n\n")
    return list_cont


def del_contact():
    list_ = export_data()
    del_ = v.print_del_cont()
    if del_ != None:
        list_.pop(del_)
        new_str = "\n\n".join(list_)

        with open('Telefon_Book.txt', 'w', encoding='utf-8') as file:
            file.write(new_str)
        v.print_del()
    else:
        v.print_exit()
