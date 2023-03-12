def print_menu():
    print("This is a phone number list. Choose an event to complete something:\n"
    "1. Open the file\n"
    "2. Save the file\n"
    "3. Show the contacts\n"
    "4. Add the contact\n"
    "5. Replace the contact\n"
    "6. Find the contact\n"
    "7. Delete the contact\n"
    "8. Exit")
    
    data = int(input("Type the number for specific event: "))
    return data

User_choice = print_menu()
phone_book = [ ]

while True:
    User_choice = print_menu()
    def open_phone_book():
                with open("phone_book.txt", "r", encoding = "utf-8") as data:
                   phone_book = data.readlines()
                   print("Opening file")
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
        if len(phone_book) == 0:
            print("you didnt open the file or it doesnt exist")
        else:
            user_info = input("Type the new contact: ")
            user_info = ";".join(user_info.split(" "))
            phone_book.append("\n" + user_info)

    def change_phone_book():
                user_info = input("Type the phone number or data you want to replace: ")
                for i in range(len(phone_book)):
                    if user_info in phone_book[i]:
                        print(phone_book[i])
                        print(i)
                        new_user_info = input("Type the new data for the contact: ")
                        phone_book[i] = phone_book[i].replace(phone_book[i], ";".join(new_user_info.split(" ")))

    def find_phone_book():
                user_info = input("Type the number or data you want to find: ")
                for i in range(len(phone_book)):
                    if user_info in phone_book[i]:
                        print(phone_book[i])
    
    def delete_phone_book():
                user_info = input("Type the number or data you want to delete: ")
                for i in range(len(phone_book)):
                    if user_info in phone_book[i]:
                        print(phone_book[i])
                        question = input("do you really want to delete it? y or n?: ")
                        if question == "y":
                            phone_book.pop(i)
    match User_choice:
        case 1:
            phone_book = open_phone_book()
        case 2:
            print("Saving")
            save_phone_book()
        case 3:
            print("Showing")
            show_phone_book()
        case 4:
            print("Adding")
            add_phone_book()

        case 5:
            print("Changing")
            change_phone_book()

        case 6:
            print("Finding")
            find_phone_book()

        case 7:
            print("Deleting")
            delete_phone_book()
            
        case 8:
            print("Exiting the system")
            break