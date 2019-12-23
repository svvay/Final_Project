class Contact_book:
    def __init__(self,
                 name,
                 surname,
                 gender=None,
                 phone=None,
                 mail=None,
                 address=None,
                 ):

        self.name = name
        self.surname = surname
        self.gender = gender
        self.phone = phone
        self.mail = mail
        self.address = address



# class Contact_book:
#     def __init__(
#             self,
#             first_name,
#             second_name,
#              age=None,
#              status=None,
#              gender=None,
#              phone_number=None,
#              work=None,
#              university=None,
#              hobbies=None,
#              home_address=None,
#              city=None,
#              countries=None,
#     ):
#         self.first_name = self.check_name(name=first_name)
#         self.second_name = self.check_name(name=second_name)
#
#     def search(self, first_name, second_name):
#         pass
#
#     def check_name(self, name):
#         if len(name) < 3:
#             raise ValueError
#         return name
#
#     def write_contact(self):
#         return {
#             'first_name': self.first_name,
#             'second_name': self.second_name,
#             # 'age': self.age,
#             # 'status': self.status,
#             # 'gender': self.gender,
#             # 'phone_number': self.phone_number,
#             # 'work': self.work,
#             # 'university': self.university,
#             # 'hobbies': self.hobbies,
#             # 'home_address': self.home_address,
#             # 'city': self.city,
#             # 'countries': self.countries,
#         }
