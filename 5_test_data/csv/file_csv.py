import csv
from csv import DictReader


def open_zip_file(file_name: str) -> dict:
    users_dict: dict = {}
    with open(file_name, newline='') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)

        for row in reader:
            users_dict = dict(zip(header, row))
    return users_dict


def open_zip_with_dict_reader(file_name: str) -> dict:
    users_dict: dict = {}
    with open(file_name, newline='') as csv_file:
        reader = DictReader(csv_file)

        for row in reader:
            users_dict = row
    return users_dict


if __name__ == "__main__":
    print(open_zip_with_dict_reader("users.csv"))
