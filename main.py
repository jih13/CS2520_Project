import tkinter as tk
from tkinter import *
from tkinter import ttk


class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x400")
        self.menubar()
        self.tabs()

    def menubar(self):
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)
        file = Menu(my_menu)
        my_menu.add_cascade(label="File", menu=file)
        file.add_command(label="Exit", command=root.quit)
        view = Menu(my_menu)  # create view menu
        my_menu.add_cascade(label="View", menu=view)
        view.add_command(label="Daily Summary", command=self.daily_summary)
        view.add_command(label="Monthly Summary", command=self.monthly_summary)

    def tabs(self):
        my_tab = ttk.Notebook(self.root)
        my_tab.pack(fill='both', expand=1)
        screen1 = Frame(my_tab, width=600, height=400, bg='light blue')
        screen2 = Frame(my_tab, width=600, height=400)
        screen1.pack(fill="both", expand=1)
        screen2.pack(fill="both", expand=1)
        my_tab.add(screen1, text="Add Expense")
        my_tab.add(screen2, text="View Summary")

        # ADD EXPENSE TAB(screen1)

        # Date Entry
        self.dateEntry = Entry(screen1)
        self.dateEntry.grid(row=0, column=1, padx=5, pady=5)
        dateEntrylabel = Label(screen1, text="Date Of Expense (mm-dd-yyyy):")
        dateEntrylabel.grid(row=0, column=0, padx=5, pady=5)

        # Amount Entry
        self.amountEntry = Entry(screen1)
        self.amountEntry.grid(row=1, column=1, padx=5, pady=5)
        amountEntrylabel = Label(screen1, text="Amount Spent:")
        amountEntrylabel.grid(row=1, column=0, padx=5, pady=5)

        # Description Entry
        self.descriptionEntry = Entry(screen1)
        self.descriptionEntry.grid(row=2, column=1, padx=5, pady=5)
        descriptionEntrylabel = Label(screen1, text="Description:")
        descriptionEntrylabel.grid(row=2, column=0, padx=5, pady=5)

        # Categories dropdown
        categories = ["Bills", "Shopping", "Groceries", "Food", "Transportation", "Entertainment"]
        category = ttk.Label(screen1, text="Category:")
        category.grid(row=3, column=0, pady=5)
        self.categorydropdown = ttk.Combobox(screen1, values=categories)
        self.categorydropdown.grid(row=3, column=1, pady=5)

        # submission button
        button = Button(screen1, text='Submit', command=self.submit_expense)
        button.grid(row=4, column=1, pady=10)

        # VIEW SUMMARY TAB (screen2)

        viewSummaryLabel = ttk.Label(screen2, text="Summary of Expenses", font=('Times', 18, 'bold'))
        viewSummaryLabel.grid(row=0, column=0, padx=5, pady=5)
        placeholder_label = ttk.Label(screen2, text="Placeholder")
        placeholder_label.grid(row=1, column=0, padx=5, pady=5)

    def daily_summary(self):
        screen3 = Toplevel(self.root)
        screen3.title("Daily Summary")
        screen3.geometry("600x400")
        screen3_label = ttk.Label(screen3, text="Daily Summary", font=('Times', 18, 'bold'))
        screen3_label.grid(row=0,column=0,padx=5,pady=5)
        placeholder_label = ttk.Label(screen3, text="Placeholder")
        placeholder_label.grid(row=1, column=0, padx=5, pady=5)

    def monthly_summary(self):
        screen4 = Toplevel(self.root)
        screen4.title("Monthly Summary")
        screen4.geometry("600x400")
        screen4_label = ttk.Label(screen4, text="Monthly Summary", font=('Times', 18, 'bold'))
        screen4_label.grid(row=0, column=0, padx=5, pady=5)
        placeholder_label = ttk.Label(screen4, text="Placeholder")
        placeholder_label.grid(row=1, column=0, padx=5, pady=5)

    def submit_expense(self):
        date = self.dateEntry.get()
        amount = self.amountEntry.get()
        description = self.descriptionEntry.get()
        category = self.categorydropdown.get()


if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
