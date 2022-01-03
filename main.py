import csv
import pandas as pd
import numpy as np
import seaborn as sns


def load_csv(filename):
    file = open(filename, 'r', encoding="utf-8")
    expenses = []
    reader = csv.reader(file)
    for i, lines in enumerate(reader):
        if i == 0:
            headers = [e.lower() for e in lines]
        else:
            line_temp = [''.join(lines)]
            tmp = line_temp[0].lower().split(";")
            tmp[4] = kr_to_float(tmp[4])
            tmp[5] = kr_to_float(tmp[5])
            expenses.append(tmp)
    file.close()
    return headers, expenses


def kr_to_float(string_):
    kronas = float(string_.replace("kr", "").replace(" ", ""))
    return kronas/100


if __name__ == '__main__':
    _, data = load_csv("Expenses.csv")
    df = pd.DataFrame(data, columns=["Date", "Text", "Type", "Budgetgroup", "Belopp", "Saldo"])
    grouped = df.groupby('Text').Belopp.sum().sort_values(ascending=True)
    df_expenses_per_store = grouped.to_frame()
    print(df_expenses_per_store)


