def main_menu():
    print('\n1: Показать контакты')
    print('2: Открыть файл телефонной книги')
    print('3: Сохранить файл телефонной книги')
    print('4: Добавить контакт')
    print('5: Изменить контакт')
    print('6: Удалить контакт')
    print('7: Найти контакт')
    print('8: Сортировать контакты')
    print('0: Выход\n')
    return choice_menu()


def choice_menu():
    while True:
        try:
            choice = int(input('Введите цифру: '))
            if choice in range(0, 9):
                return choice
            else:
                print('Такой цифры в меню нет')
        except:
            print('Некорректные данные, попробуйте снова')


def log_off():
    print('До свидания.')


def load_success():
    print('Телефонная книга загружена.')


def save_success():
    print('Телефонная книга сохранена.')


def remove_success():
    print('Контакт удалён.')


def print_book_list(book_list: list):
    if len(book_list) > 0:
        for id, contact in enumerate(book_list, 1):
            print(id, *contact)
    else:
        print('Телефонная книга пуста / не загружена')


def input_new_contact():
    name = input('Введите имя контакта: ')
    while True:
        phone = input('Введите номер контакта: ')
        if phone.isdigit():
            break
        else:
            print('Номер может состоять только из цифр')
    while True:
        comment = input('Введите комментарий к контакту: ')
        if comment in ['учёба', 'другое', 'друг', 'враг', 'работа', 'родственники']:
            break
        else:
            print('Комментарий может быть только: учёба, другое, друг, враг, работа, родственники')
    return [name, phone, comment]


def input_remove_contact():
    id = int(input('Введите id контакта который хотите удалить: '))
    return id


def input_change_id():
    id = int(input('Введите id контакта который хотите изменить: '))
    return id


def input_change_contact():
    name = input('Введите имя контакта: ')
    while True:
        phone = input('Введите номер контакта: ')
        if phone.isdigit():
            break
        else:
            print('Номер может состоять только из цифр')
    while True:
        comment = input('Введите комментарий к контакту: ')
        if comment in ['учёба', 'другое', 'друг', 'враг', 'работа', 'родственники']:
            break
        else:
            print('Комментарий может быть только: учёба, другое, друг, враг, работа, родственники')
    return [name, phone, comment]


def change_success():
    print('Контакт изменён.')


def new_contact_success():
    print('Контакт добавлен.')


def deny_operation():
    print('Операция отменена')


def find_contact():
    search = input('Введите имя, телефон, или комментарий для поиска: ')
    return search


def not_found():
    print('Совпадений не найдено.')




def choice_sorted_key():
    while True:
        print('\n1: Сортировка по имени')
        print('2: Сортировка по номеру')
        print('3: Сортировка по комментарию')
        print('0: Выход\n')
        try:
            choice = int(input(' Введите цифру: '))
            if choice in range(0, 4):
                return choice
            else:
                print('Такой цифры нет')
        except:
            print('некорректные данные')



