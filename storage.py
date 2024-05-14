from entities import AddressBook, Name, Phone, Id, Birthday

def add_user_to_store(name, phone):
  id_record = Id()
  name_record = Name(name)
  phone_record = Phone(phone) 
  new_record = address_book.add_record(id_record, name_record, phone_record)

  return new_record

def find_all_users_from_store():
  return address_book.get_records()

def update_user_by_id(id, new_name, new_phone):
  return address_book.update_record_by_id(id, new_name, new_phone)

def get_user_phone_by_name(name):
  phone = address_book.get_record_by_field("Name", name, "Phone")
  return phone

def add_birthday_to_user(id, date):
  birthday = Birthday(date)
  return address_book.add_birthday_by_id(id, birthday)

def get_birthday_by_name(name):
  return address_book.get_record_by_field("Name", name, "Birthday")

def get_birthdays():
  return address_book.get_upcoming_birthdays()

address_book = AddressBook()
address_book.add_record(Id(), Name("John"), Phone("+380501234567"));
