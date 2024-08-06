import tkinter as tk
from tkinter import Menu, Toplevel
from tkinter import ttk
import sqlite3

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x400")
        self.menubar()
        self.tabs()
        self.db_connection = self.connect_to_db()  # Establish a connection to the database

    def menubar(self):
        my_menu = Menu(self.root)
        self.root.config(menu=my_menu)
        file = Menu(my_menu)
        my_menu.add_cascade(label="File", menu=file)
        file.add_command(label="Exit", command=self.root.quit)
        view = Menu(my_menu)  # Create view menu
        my_menu.add_cascade(label="View", menu=view)
        view.add_command(label="Daily Summary", command=self.daily_summary)
        view.add_command(label="Monthly Summary", command=self.monthly_summary)
        view.add_command(label="Category Summary", command=self.category_summary)  # Add category summary view

    def tabs(self):
        my_tab = ttk.Notebook(self.root)
        my_tab.pack(fill='both', expand=1)
        screen1 = ttk.Frame(my_tab, width=600, height=400)
        screen2 = ttk.Frame(my_tab, width=600, height=400)
        screen1.pack(fill="both", expand=1)
        screen2.pack(fill="both", expand=1)
        my_tab.add(screen1, text="Add Expense")
        my_tab.add(screen2, text="View Summary")

        # ADD EXPENSE TAB (screen1)

        # Date Entry
        self.dateEntry = ttk.Entry(screen1)
        self.dateEntry.grid(row=0, column=1, padx=5, pady=5)
        dateEntrylabel = ttk.Label(screen1, text="Date Of Expense (YYYY-MM-DD):")
        dateEntrylabel.grid(row=0, column=0, padx=5, pady=5)

        # Amount Entry
        self.amountEntry = ttk.Entry(screen1)
        self.amountEntry.grid(row=1, column=1, padx=5, pady=5)
        amountEntrylabel = ttk.Label(screen1, text="Amount Spent:")
        amountEntrylabel.grid(row=1, column=0, padx=5, pady=5)

        # Description Entry
        self.descriptionEntry = ttk.Entry(screen1)
        self.descriptionEntry.grid(row=2, column=1, padx=5, pady=5)
        descriptionEntrylabel = ttk.Label(screen1, text="Description:")
        descriptionEntrylabel.grid(row=2, column=0, padx=5, pady=5)

        # Categories dropdown
        categories = ["Bills", "Shopping", "Groceries", "Food", "Transportation", "Entertainment"]
        category = ttk.Label(screen1, text="Category:")
        category.grid(row=3, column=0, pady=5)
        self.categorydropdown = ttk.Combobox(screen1, values=categories)
        self.categorydropdown.grid(row=3, column=1, pady=5)

        # Submission button
        button = ttk.Button(screen1, text='Submit', command=self.submit_expense)
        button.grid(row=4, column=1, pady=10)

        # VIEW SUMMARY TAB (screen2)

        viewSummaryLabel = ttk.Label(screen2, text="Summary of Expenses", font=('Times', 18, 'bold'))
        viewSummaryLabel.grid(row=0, column=0, padx=5, pady=5)
        placeholder_label = ttk.Label(screen2, text="Use the 'View' menu to see summaries")
        placeholder_label.grid(row=1, column=0, padx=5, pady=5)

    def connect_to_db(self):
        # Connect to SQLite database (or create it if it doesn't exist)
        connection = sqlite3.connect('expenses.db')
        cursor = connection.cursor()
        # Create expenses table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY,
                date TEXT,
                category TEXT,
                amount REAL,
                description TEXT
            )
        ''')
        connection.commit()
        return connection

    def submit_expense(self):
        date = self.dateEntry.get()
        amount = self.amountEntry.get()
        description = self.descriptionEntry.get()
        category = self.categorydropdown.get()

        # Insert the expense into the database
        cursor = self.db_connection.cursor()
        cursor.execute('''
            INSERT INTO expenses (date, category, amount, description)
            VALUES (?, ?, ?, ?)
        ''', (date, category, amount, description))
        self.db_connection.commit()

        # Clear the form fields
        self.dateEntry.delete(0, tk.END)
        self.amountEntry.delete(0, tk.END)
        self.descriptionEntry.delete(0, tk.END)
        self.categorydropdown.set('')

        print("Expense submitted:", date, category, amount, description)

    def daily_summary(self):
        from summary import Summary
        summary = Summary(self.db_connection)
        daily_summary = summary.get_daily_summary()

        # Create a new window for displaying daily summary
        screen3 = Toplevel(self.root)
        screen3.title("Daily Summary")
        screen3.geometry("600x400")
        screen3_label = ttk.Label(screen3, text="Daily Summary", font=('Times', 18, 'bold'))
        screen3_label.grid(row=0, column=0, padx=5, pady=5)

        row_num = 1
        for date, total in daily_summary:
            summary_label = ttk.Label(screen3, text=f"{date}: ${total:.2f}")
            summary_label.grid(row=row_num, column=0, padx=5, pady=5)
            row_num += 1

        # Add button to plot daily summary
        plot_button = ttk.Button(screen3, text="Plot Daily Summary", command=summary.plot_daily_summary)
        plot_button.grid(row=row_num, column=0, padx=5, pady=5)

    def monthly_summary(self):
        from summary import Summary
        summary = Summary(self.db_connection)
        monthly_summary = summary.get_monthly_summary()

        # Create a new window for displaying monthly summary
        screen4 = Toplevel(self.root)
        screen4.title("Monthly Summary")
        screen4.geometry("600x400")
        screen4_label = ttk.Label(screen4, text="Monthly Summary", font=('Times', 18, 'bold'))
        screen4_label.grid(row=0, column=0, padx=5, pady=5)

        row_num = 1
        for month, total in monthly_summary:
            summary_label = ttk.Label(screen4, text=f"{month}: ${total:.2f}")
            summary_label.grid(row=row_num, column=0, padx=5, pady=5)
            row_num += 1

        # Add button to plot monthly summary
        plot_button = ttk.Button(screen4, text="Plot Monthly Summary", command=summary.plot_monthly_summary)
        plot_button.grid(row=row_num, column=0, padx=5, pady=5)

    def category_summary(self):
        from summary import Summary
        summary = Summary(self.db_connection)
        category_summary = summary.get_category_summary()

        # Create a new window for displaying category summary
        screen5 = Toplevel(self.root)
        screen5.title("Category Summary")
        screen5.geometry("600x400")
        screen5_label = ttk.Label(screen5, text="Category Summary", font=('Times', 18, 'bold'))
        screen5_label.grid(row=0, column=0, padx=5, pady=5)

        row_num = 1
        for category, total in category_summary:
            summary_label = ttk.Label(screen5, text=f"{category}: ${total:.2f}")
            summary_label.grid(row=row_num, column=0, padx=5, pady=5)
            row_num += 1

        # Add button to plot category summary
        plot_button = ttk.Button(screen5, text="Plot Category Summary", command=summary.plot_category_summary)
        plot_button.grid(row=row_num, column=0, padx=5, pady=5)
        
def export_to_json(self):
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()

        expenses_list = []
        for expense in expenses:
            expense_dict = {
                'id': expense[0],
                'date': expense[1],
                'category': expense[2],
                'amount': expense[3],
                'description': expense[4]
                        }
            expenses_list.append(expense_dict)

        with open('expenses.json', 'w') as json_file:
            json.dump(expenses_list, json_file, indent=4)
        print("Expenses exported to expenses.json")

    def import_from_json(self):
        with open('expenses.json', 'r') as json_file:
            expenses_list = json.load(json_file)

        cursor = self.db_connection.cursor()
        for expense in expenses_list:
            cursor.execute('''
                INSERT OR IGNORE INTO expenses (id, date, category, amount, description)
                VALUES (?, ?, ?, ?, ?)
            ''', (expense['id'], expense['date'], expense['category'], expense['amount'], expense['description']))
        self.db_connection.commit()
        print("Expenses imported from expenses.json")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()
