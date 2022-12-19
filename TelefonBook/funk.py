import view as v
import csv


def import_book():
    name_ = input(
        'Введите имя файла, из которого импортируется телефонная книга - ')
    with open(f'{name_}.txt', 'r') as f:
        data_Book = f.read()

    with open('Telefon_Book.csv', 'a+') as f:
        f.write(data_Book + '\n\n')
    v.print_import_book(name_)


def add_contact(surname, first_name, patronymic, phone_number):
    with open('Telefon_Book.csv', 'a+', encoding='utf-8') as f:
        f.write(surname + '\n' + first_name + '\n' +
                patronymic + '\n' + phone_number + '\n\n')


def search_data(word, data_list):
    if len(data_list) > 0:
        resalt = []
        count = 0
        for item in data_list:
            if word in item:
                resalt.append(item)
                resalt.append(count)
            count += 1
        return resalt
    else:
        return None


def export_data():
    
    with open('Telefon_Book.csv', newline='', encoding='utf-8') as file:
        data_reader = csv.reader(file, skipinitialspace=True)
        data_list = list(data_reader)

         
    return data_list


def del_contact():
    list_ = export_data()
    del_ = v.print_del_cont()
    util = list_.pop(del_)
    new_str = "\n".join(str(x) for x in list_)
    

    with open('Telefon_Book.csv', 'w+', newline='', encoding='utf-8') as file:
        file_writer = csv.writer(file)
        file_writer.writerow([new_str])
    return util
