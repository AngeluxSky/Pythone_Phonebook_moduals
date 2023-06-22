import text
import view
import module
def start():
    while True:
        select = view.menu()
        match select:
            case 1:
                if module.open_file():
                    view.print_message(text.load_successful)
                else:
                    view.print_message(text.error_load)
            case 2:
                if module.save_file():
                    view.print_message(text.save_successful)
                else:
                    view.print_message(text.error_save)
            case 3:
                view.show_contacts(module.phone_book, text.empty_book)
            case 4:
                new = view.add_contact_new()
                module.add_contact(new)
                view.print_message(text.add_successful(new.get('name')))
            case 5:
                word = view.search_word()
                result = module.search(word)
                view.show_contacts(result, text.empty_search(word))
            case 6:
                view.show_contacts(module.phone_book, text.empty_book)
                second = view.change_contact()
                new_data = view.add_contact_new()
                module.edit_contact(second, new_data)
            case 7:
                view.show_contacts(module.phone_book, text.empty_book)
                number = view.delete_contact()
                module.delete_contact(number)
            case 8:
                view.print_message(text.exit_menu)
                break