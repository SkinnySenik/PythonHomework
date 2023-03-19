def menu() -> int :
    print("""Main Menu:
    1. Open the file
    2. Save the file
    3. Show the contacts
    4. Add the contact
    5. Change the contact
    6. Find the contact
    7. Delete the contact
    8. Exit """)
    choice = int(input("choose the setting:"))
    return choice


def show_contact(phone_book: dict):
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}.{contact.get("name"):<20} '
            f'{contact.get("phone"):<20} '
            f'{contact.get("comment"):<20}')
    else:
        print("\nyou didnt open the file or it doesnt exist\n")

def input_request(text: str) -> str:
        return input(f"type {text}: ")

def new_contact() -> dict:
    print()
    name = input("type name: ")
    phone = input("type the phone: ")
    comment = input("type the kind: ")
    print()
    return {"name": name, "phone": phone, "comment": comment}

def change_contact(book: list) -> tuple:
    show_contact(book)
    choice = int(input("type the object you will change: "))
    name = input("type replacing name: ")
    phone = input("type the replacing phone: ")
    comment = input("type the replacing kind: ")
    return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                       'phone': phone if phone else book[choice - 1].get('phone'),
                       'comment': comment if comment else book[choice - 1].get('comment')}

def select_to_delete(book: list):
    show_contact(book)
    return int(input("type the index of element you want to delete: ")) - 1

