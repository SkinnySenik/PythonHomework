class PhoneBook:
    
    def __init__(self, path: str = "phone_book.txt"):
        self.path = path
        self.phone_book = []

    def open(self):
        with open(self.path, "r", encoding = "UTF-8") as file:
           data = file.readlines()
           print(data)
           for  contact in data:
               pb = {}
               new = contact.strip().split(";")
               pb["name"] = new[0]
               pb["phone"] = new[1]
               pb["comment"] = new[2]
               self.phone_book.append(pb)
    
    def save(self):
        data = []
        for contact in self.phone_book:
            data.append(";".join(contact.values()))
        data = "\n".join(data)
        with open(self.path, "w", encoding = "UTF-8") as file:
            file.write(data)

    def get(self):
        return self.phone_book

    def new_contact(self, contact: dict):
        self.phone_book.append(contact)
        print(f'\n contact {contact.get("name")} is successfully written down')

    def search(self, word: str) -> dict:
        search_result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    search_result.append(contact)
        return search_result
    
    def change(self, i: int, new_value: dict):
        self.phone_book[i] = new_value

    def delete(self, i: int):
        contact = self.phone_book.pop(i)
        print(f'\n contact {contact.get("name")} is successfully deleted')

