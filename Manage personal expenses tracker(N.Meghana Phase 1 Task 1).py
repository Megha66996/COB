###N.MEGHANA 21BCE9935 PHASE-2 TASK 1

import tkinter as tk
from tkinter import ttk
import datetime
import json

app = tk.Tk()
app.title("Expense Tracker")

expenses = []


def add_expense():
    date = entry_date.get()
    category = entry_category.get()
    amount = entry_amount.get()
    expenses.append({"date": date, "category": category, "amount": amount})
    update_expense_list()
    entry_date.delete(0, "end")
    entry_category.delete(0, "end")
    entry_amount.delete(0, "end")


def update_expense_list():
    expense_list.delete(0, "end")
    for expense in expenses:
        expense_list.insert("end", f"{expense['date']} | {expense['category']} | ${expense['amount']}")

def generate_report():
    selected_month = combo_month.get()
    selected_year = combo_year.get()
    total_expense = 0
    for expense in expenses:
        date = datetime.datetime.strptime(expense["date"], "%Y-%m-%d")
        if date.month == selected_month and date.year == selected_year:
            total_expense += float(expense["amount"])
    label_report.config(text=f"Total Expenses for {selected_month}/{selected_year}: ${total_expense:.2f}")


def save_to_file():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def load_from_file():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
        update_expense_list()
    except FileNotFoundError:
        pass


label_date = ttk.Label(app, text="Date (YYYY-MM-DD):")
entry_date = ttk.Entry(app)
label_category = ttk.Label(app, text="Category:")
entry_category = ttk.Entry(app)
label_amount = ttk.Label(app, text="Amount ($):")
entry_amount = ttk.Entry(app)
button_add = ttk.Button(app, text="Add Expense", command=add_expense)

expense_list = tk.Listbox(app, height=10)
scrollbar = ttk.Scrollbar(app, orient="vertical", command=expense_list.yview)
expense_list.configure(yscrollcommand=scrollbar.set)

label_month = ttk.Label(app, text="Select Month:")
combo_month = ttk.Combobox(app, values=list(range(1, 13)))
label_year = ttk.Label(app, text="Select Year:")
combo_year = ttk.Combobox(app, values=list(range(2000, 2051)))
button_report = ttk.Button(app, text="Generate Report", command=generate_report)
label_report = ttk.Label(app, text="")


load_from_file()


label_date.grid(row=0, column=0)
entry_date.grid(row=0, column=1)
label_category.grid(row=1, column=0)
entry_category.grid(row=1, column=1)
label_amount.grid(row=2, column=0)
entry_amount.grid(row=2, column=1)
button_add.grid(row=3, column=0, columnspan=2)

expense_list.grid(row=4, column=0, columnspan=2)
scrollbar.grid(row=4, column=2)

label_month.grid(row=5, column=0)
combo_month.grid(row=5, column=1)
label_year.grid(row=5, column=2)
combo_year.grid(row=5, column=3)
button_report.grid(row=6, column=0, columnspan=4)
label_report.grid(row=7, column=0, columnspan=4)

app.protocol("WM_DELETE_WINDOW", save_to_file)

app.mainloop()