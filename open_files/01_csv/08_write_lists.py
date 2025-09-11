import csv
from os import path


def write_csv(file, headers, rows):
    with open(file, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(headers)
        csvwriter.writerows(rows)


if __name__ == "__main__":
    headers = [
        "id",
        "first_name",
        "last_name",
        "email_address",
        "gender",
        "yearly_salary",
        "years_of_experience",
    ]

    rows = [
        [1, "John", "Doe", "john.doe@company.com", "Male", 120000, 9],
        [2, "Jane", "Doe", "jane.doe@company.com", "Female", 90000, 3],
    ]

    # name of csv file
    filename = "./files/employees-backup-1.csv"

    # Write the CSV file
    write_csv(filename, headers, rows)
