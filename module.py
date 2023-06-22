import json

phone_book = {}
path = 'phone.json'

def open_file():
    global phone_book
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            phone_book = json.load(file)
        return True
    except:
        return False

def save_file():
    global phone_book
    try:
        with open(path, 'w', encoding='UTF-8') as file:
            json.dump(phone_book, file, ensure_ascii=False)
        return True
    except:
        return False

def search(word: str) -> dict[int:dict[str,str]]:
    result = {}
    for index, contact in phone_book.items():
        if word.lower() in ' '.join(contact.values()).lower():
            result[index] = contact
    return result
def check_id():
    if phone_book:
        return max(list(map(int, phone_book))) + 1
    return 1
def add_contact(new: {int: dict[str,str]}):
    global phone_book
    contact = {check_id(): new}
    phone_book.update(contact)

def show_contacts(book: dict[int, dict[str,str]], message: str):
    print(message)
    for index, contact in phone_book.items():
        print(f"{id}. {contact['name']} - {contact['phone']} - {contact['email']}")

def edit_contact(second: int, new_data: dict[int, dict[str,str]]):
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = json.load(file)
    if str(second) not in phone_book:
        print('Контакт с таким ID не найден!')
        return

    phone_book[str(second)].update(new_data)
    print('Контакт успешно изменен!')
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(phone_book, file, ensure_ascii=False)

def delete_contact(number: int):
    global phone_book
    with open(path, 'r', encoding='UTF-8') as file:
        phone_book = json.load(file)
    if str(number) not in phone_book:
        print('Контакт с таким ID не найден!')
        return

    del phone_book[str(number)]
    print('Контакт успешно удален!')
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(phone_book, file, ensure_ascii=False)