import view as v

def import_book():
    name = input('Введите имя файла, из которого импортируется телефонная книга - ')
    with open (f'{name}.txt', 'r') as f:
        data_Book = f.read()
        # print(list(data_Book))
    with open ('Telefon_Book.txt', 'a') as f:
        f.write(data_Book + '\n\n')

import_book()
