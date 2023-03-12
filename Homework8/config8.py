phone_book = [ ]

def open_phone_book():
    with open("phone_book.txt", "r", encoding = "utf-8") as data:
        phone_book = data.readlines()
        print("opening")
        return phone_book

def save_phone_book():
    with open("phone_book.txt", "w", encoding = "utf-8") as data:
        for i in phone_book:
            data.write(i)

def show_phone_book():
    print(phone_book)
    if len(phone_book) == 0:
        print("you didnt open the file or it doesnt exist")
    else:
        for i in phone_book:
            print(" ".join(i.split(";")))

def add_phone_book():
        user_info = input("Type the new contact: ")
        user_info = ";".join(user_info.split(" "))
        phone_book.append("\n" + user_info)

def change_phone_book():
    user_info = input("Type the phone number you want to replace: ")
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            print(i)
            new_user_info = input("Type the new number for the contact: ")
            phone_book[i] = phone_book[i].replace(phone_book[i], new_user_info)

def find_phone_book():
    user_info = input("Type the number you want to find: ")
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])

def delete_phone_book():
    user_info = input("Type the number you want to delete: ")
    for i in range(len(phone_book)):
        if user_info in phone_book[i]:
            print(phone_book[i])
            question = input("do you really want to delete it? y or n?: ")
            if question == "y":
                phone_book.pop(i)

phone_book = open_phone_book()
# add_phone_book()
# show_phone_book()
# change_phone_book()
# delete_phone_book()
# save_phone_book()