from csv import csv


def read_csv_gen(path):
    with open(path, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            yield row


# iterate over generator
# content = [row for row in read_csv_gen("generators/users.csv")]

result = read_csv_gen("generators/users.csv")
# get only first row
print(next(result))
