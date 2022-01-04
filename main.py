import csv
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

label_format = '{:,.0f}'

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


def expenses_by_store(df, a, b):
    updated_df = df.groupby(['Text'])['Belopp'].sum().reset_index().sort_values("Belopp", ascending=True)
    updated_df.drop(updated_df.tail(1).index, inplace=True)
    updated_df = updated_df.reset_index(drop=True)
    updated_df = updated_df.drop([updated_df.index[i] for i in range(a, b)])
    return updated_df


def plot_expenses_by_store(xx, yy):
    g = sns.barplot(x=xx, y=yy)
    g.set_xticklabels(labels=df_expense['Text'], rotation=70, fontsize=7.5, fontweight="bold")
    ticks_loc = g.get_yticks().tolist()
    g.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
    g.set_yticklabels([label_format.format(x) for x in ticks_loc], fontsize=7.5, fontweight="bold")
    g.set_ylabel("Money", color="black", fontsize=15)
    g.set_xlabel("Store", color="black", fontsize=15)
    plt.subplots_adjust(bottom=0.35)


if __name__ == '__main__':
    _, data = load_csv("Expenses.csv")
    df = pd.DataFrame(data, columns=["Date", "Text", "Type", "Budgetgroup", "Belopp", "Saldo"])
    df_expense = expenses_by_store(df, 25, 210)
    plot_expenses_by_store(df_expense['Text'], df_expense['Belopp'])
    plt.show()

