from operator import itemgetter

book_list = []


def get_book_list():
    global book_list
    return book_list


def set_book_list(list):
    global book_list
    book_list = list


def add_contact(contact: list):
    global book_list
    book_list.append(contact)


def remove_contact(id):
    global book_list
    name = book_list[id - 1][0]
    confirm = input(f'Вы действительно хотите удалить контакт {name}? (yes / no): ')
    if confirm.lower() == 'yes':
        book_list.pop(id - 1)
        return True
    else:
        return False


def change_contact(id, contact):
    global book_list
    name = book_list[id - 1]
    confirm = input(f'Вы действительно хотите изменить контакт {name}? (yes / no): ')
    if confirm.lower() == 'yes':
        book_list[id - 1][0] = contact[0]
        book_list[id - 1][1] = contact[1]
        book_list[id - 1][2] = contact[2]
        return True
    else:
        return False


def search_contact(string: str):
    count = 0
    for contact in book_list:
        for item in contact:
            if item.find(string) != -1:
                print(*contact)
                count += 1
    if count > 0:
        return True


def sorted_phone_book(key):
    global book_list
    match key:
        case 1:
            book_list = sorted(book_list, key=itemgetter(0))
            print(book_list)
            return book_list
        case 2:
            book_list = sorted(book_list, key=itemgetter(1))
            print(book_list)
            return book_list
        case 3:
            book_list = sorted(book_list, key=itemgetter(2))
            print(book_list)
            return book_list
        case 0:
            return book_list
