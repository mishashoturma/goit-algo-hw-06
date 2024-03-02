from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass
    

class Phone(Field):
    def check(self):
        lenght = self
        if len(lenght) == 10:
            return self
        else: "Номер містить хибну кількість цифр"


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(str(Phone.check(phone)))
    
    def remove_phone(self, phone):
        if phone in self.phones:
            self.phones.remove(phone)
    
    def edit_phone(self, old, new):
        if old in self.phones:
            self.phones.remove(old)
        self.phones.append(str(Phone.check(new)))
    
    def find_phone(self, phone):
        for phone in self.phones:
            if phone in self.phones:
                return phone
        

class AddressBook(UserDict):
    def add_record(self, kontact):
        self.data[kontact.name.value]=kontact
        
    def find(self, name):
        return self.data.get(name)
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
    



# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")

