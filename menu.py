import view
import phone_book as pb
import data_base as db


def optional_functionality(choice: int):
    match choice:
        case 1:
            phone_book = pb.get_book_list()
            view.print_book_list(phone_book)
        case 2:
            db.load_data_base()
            view.load_success()
        case 3:
            db.save_data_base()
            view.save_success()
        case 4:
            contact = view.input_new_contact()
            pb.add_contact(contact)
            view.new_contact_success()
        case 5:
            phone_book = pb.get_book_list()
            view.print_book_list(phone_book)
            id = view.input_change_id()
            contact = view.input_change_contact()
            if pb.change_contact(id, contact):
                view.change_success()
            else:
                view.deny_operation()
        case 6:
            phone_book = pb.get_book_list()
            view.print_book_list(phone_book)
            id = view.input_remove_contact()
            if pb.remove_contact(id):
                view.remove_success()
            else:
                view.deny_operation()
        case 7:
            search = view.find_contact()
            if pb.search_contact(search):
                pass
            else:
                view.not_found()
        case 8:
            key = view.choice_sorted_key()
            pb.sorted_phone_book(key)
        case 0:
            return True


def strat():
    while True:
        choice = view.main_menu()
        if optional_functionality(choice):
            view.log_off()
            break
