if __name__ == "__main__":
    with open('example.txt', "w") as f:
        for n in range(10):
            f.write(str(n) + "\n")
