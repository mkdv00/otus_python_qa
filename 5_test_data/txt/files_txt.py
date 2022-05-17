if __name__ == "__main__":
    with open("file.txt", 'r', encoding="utf-8") as file:
        for line in file.readlines():
            print(line)
