import view
import phone_book

pb = phone_book.PhoneBook()

def start():
    while True:
        choice = view.menu()
        match choice:
            case 1:
                print("\nopening\n")
                pb.open()

            case 2:
                print("\nsaving\n")
                pb.save()

            case 3:
                book = pb.get()
                view.show_contact(book)

            case 4:
                print("\nAdding\n")
                new_entry = view.new_contact()
                pb.new_contact(new_entry)


            case 5:
                print("\nChanging\n")
                new_value = view.change_contact(pb.get())
                pb.change(*new_value)
            
            case 6:
                print("\nFinding\n")
                word = view.input_request("index you want to find")
                result = pb.search(word)
                view.show_contact(result)

            case 7:
                print("\nDeleting\n")
                index = view.select_to_delete(pb.get())
                pb.delete(index)
            
            
            case 8:
                print("Exiting the system")
                break
        