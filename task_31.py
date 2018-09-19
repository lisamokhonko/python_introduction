#Task #31
#find_entry_age_phonebook
#print_phonebook_by_age
#delete_entry_name_phonebook
#print_avr_age
#delete_entry_under_age
import pickle


running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "email": "qwerty@gmail.com"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "email": "qwerty@yandex.ru"},
              {"name": "Semen", "surname": "Semenov", "age": 35, "phone_number":"+380500000010", "email": "qwerty@mail.ru"},
             ]

domain_to_block = ["yandex.ru", "mail.ru"]

#------------------------------------------------------------------------------
def print_entry(number, entry):
    print("--[ %s ]--------------------------" % number)
    print("| Surname: %20s |" % entry["surname"])
    print("| Name:    %20s |" % entry["name"])
    print("| Age:     %20s |" % entry["age"])
    print("| Phone:   %20s |" % entry["phone_number"])
    print("| E-mail:  %20s |" % entry["email"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    email = input("    Enter E-mail.: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["email"] = email
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)


#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("    Enter age: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

#------------------------------------------------------------------------------
def find_entry_email_phonebook():
    email = str(input("    Enter E-mail: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["email"] == email:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

def find_entry_email_to_block():
    print("E-mails that could be blocked, please update them")
    idx = 1
    found = False
    for entry in phone_book:
        if entry["email"].split('@')[1] in domain_to_block:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!")

#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name_in = input("Enter Name: ")
    len_original = len(phone_book)
    phone_book[:] = [d for d in phone_book if d.get('name') != name_in]
    if len_original > len(phone_book):
        print('Deleted')
    else:
        printError('Not found!')

#------------------------------------------------------------------------------
def delete_entry_under_age():
    adult_age = int(input("Enter Age: "))
    len_pb = len(phone_book)
    for idx in range(len_pb-1, 0, -1):
        dict = phone_book[idx]
        for key in dict:
            if key == 'age':
                if dict[key] < adult_age:
                    del phone_book[idx]
                    #idx += 1
                    len_pb -= 1
                    print('Deleted')
                else:
                    print("Not found")

#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def print_phonebook_by_age():
    #print()
    print()
    print("#########  Phone book by Age  ##########")
    #print()

    number = 1
    phone_book.sort(key=lambda elem: elem['age'])
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def increase_age():
    age_add = int(input("Enter Age to increase: "))
    number = 1
    for entry in phone_book:
        entry["age"] += age_add
        print_entry(number, entry)
        number += 1

#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    number = 1
    sum_age = 0
    for entry in phone_book:
        sum_age += entry["age"]
        number += 1
    number -= 1
    print('Average age for phonebook is %.2f years' % (sum_age/number))


#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      #print()
      #print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Find entry by e-mail")
      print("     7 - Delete entry by name")
      print("     8 - Delete data of under age people")
      print("     9 - The number of entries in the phonebook")
      print("     A - Avr. age of all persons")
      print("     B - Increase age by num. of years")
      print("     C - Find E-mails that need to be update")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  find_entry_email_phonebook,
                  '7':  delete_entry_name_phonebook,
                  '8':  delete_entry_under_age,
                  '9':  count_all_entries_in_phonebook,
                  'A':  avr_age_of_all_persons,
                  'B':  increase_age,
                  'C':  find_entry_email_to_block,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()