import json


def json_write(file_name: str, data_to_add: dict) -> None:
    with open(file_name, "w") as f:
        f.write(json.dumps(data_to_add, indent=4))


if __name__ == "__main__":
    data = {
        "users": [
            {"name": "Dominator", "skill": 100, "gold": 1000},
            {"name": "Who", "skill": 99, "gold": 9999}
        ]
    }

    json_write(file_name="example2.json", data_to_add=data)
