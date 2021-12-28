import csv


def load_csv(filename):
    file = open(filename, 'r', encoding="utf-8")
    expenses = []
    reader = csv.reader(file)
    for i, lines in enumerate(reader):
        if i == 0:
            headers = [e.lower() for e in lines]
        else:
            line_temp = [''.join(lines)]
            expenses.append(line_temp[0].lower().split(";"))
    file.close()
    return headers, expenses


def kr_to_float(string_):
    kronas = float(string_.replace("kr", "").replace(" ", ""))
    return kronas


if __name__ == '__main__':
    _, data = load_csv("Expenses.csv")
    print(data[0])
    d = kr_to_float(data[0][5])
    print(d)
