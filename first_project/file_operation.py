import contact_func, file_cont
import csv


class WriteRead:
    def __init__(self, file_name, file_extention):
        self.file_name = file_name
        self.file_extention = file_extention

    def read_file(self):
        with open(f'files/{file_cont.file_name}{file_cont.file_extention}') as fileCSV:
            return list(csv.DictReader(fileCSV))

    def write(self):
        with open(f'files/{self.file_name}{self.file_extention}', 'a') as fileCSV:
            result = contact_func.input_info()
            fieldnames = list(result.keys())
            writer = csv.DictWriter(fileCSV, fieldnames=fieldnames)
            writer.writerows([result])

        print('Add info Done')

    def finding_contact(self):
        with open(f'files/{file_cont.file_name}{file_cont.file_extention}', "r") as search:
            return list(csv.DictReader(search))
