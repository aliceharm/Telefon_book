import view as v
import funk as f


def phonebook():
    menu_item = v.menu()
    if menu_item == "1":
        v.print_adding_contact()
    elif menu_item == "2":
        f.del_contact()
        v.print_del()
    elif menu_item == "3":
        v.print_search()
    elif menu_item == "4":
        f.import_book()
    elif menu_item == "0":
        v.print_exit()
