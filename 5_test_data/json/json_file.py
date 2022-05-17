import json


def read_json_file(file_name: str) -> dict:
    with open(file_name, "r") as json_file:
        all_users = json.loads(json_file.read())
        return all_users


if __name__ == "__main__":
    users = read_json_file("example.json")
    for user in users['users']:
        print(user)
