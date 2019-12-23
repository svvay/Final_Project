import contact_func, file_operation, search_func
import file_cont


def main():
    while True:
        get_choice = input('Enter what u want to do \n'
                           'a - add contact \n'
                           's - show all contact \n'
                           'f - find contact \n'
                           'c - close contact \n').lower()

        if get_choice == 's':
            open_file = file_operation.WriteRead.read_file(None)

            for words in open_file:
                print("\n")
                for key, value in dict(words).items():
                    print(f"{key} - {value}")

        elif get_choice == 'a':
            contact_func.create_contact(file_cont.file_name, file_cont.file_extention)

        elif get_choice == 'f':
            search_func.search_func(input('Eneter what search: '))

        elif get_choice == 'c':
            print('Thanks')
            break

        else:
            print('Try more, wrong choice')


main()
