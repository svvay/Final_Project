import file_operation
import string


def create_contact(file_name, file_extention):
    file_manager = file_operation.WriteRead(file_name=file_name, file_extention=file_extention)
    contact_list = file_manager.write()
    return contact_list


def input_info():

    while True:
        input_user = {}

        while True:
            input_name = input("Please input Name: ")
            if len(input_name) > 3:
                input_user["Name"] = input_name.capitalize()
                break
            else:
                print("Please input more than 3 symbols")

        while True:
            input_surname = input("Please input Surname: ")
            if len(input_surname) > 3:
                input_user["Surname"] = input_surname.capitalize()
                break
            else:
                print("Please input more than 3 symbols")

        while True:
            input_gender = input('Eneter yours Gender please M/W: ').upper()
            if len(input_gender) == 1:
                input_user['Gender'] = input_gender.capitalize()
                break
            else:
                print('Try more, write first letter')

        while True:
            input_phone = input('Enter mobile number: ')
            if input_phone.startswith('+380') and len(input_phone) == 13:
                input_user['Phone'] = input_phone
                break
            elif input_phone.startswith('80') and len(input_phone) == 11:
                input_user['Phone'] = input_phone
                break
            elif input_phone.startswith('0') and len(input_phone) == 10:
                input_user['Phone'] = input_phone
                break
            else:
                print('Try more: ')

        while True:
            input_mail = input('Enter mail please: ')
            if input_mail.find('@') != -1:
                input_user["Mail"] = input_mail.lower()
                print()
                break
            else:
                print('Sorry try more: ')

        for dict_keys, dict_values in input_user.items():
            print(f"{dict_keys} - {dict_values}")

        while True:
            y_n = input("Save data? (y/n): ")

            if y_n == "y":
                return input_user
            elif y_n == "n":
                break
            else:
                print("Sorry try more: ")
