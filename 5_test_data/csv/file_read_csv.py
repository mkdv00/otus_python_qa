import csv


def write_to_csv(file_name: str) -> None:
    with open(file_name, "w", newline='') as csv_f:
        writer = csv.writer(csv_f, delimiter=',', )

        writer.writerow(['data', 'result', 'code'])
        for i in range(10):
            writer.writerow([i, i * 100, str(bin(i))])


if __name__ == "__main__":
    write_to_csv("example.csv")
