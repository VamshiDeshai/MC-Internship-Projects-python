import json
import os

DATA_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(DATA_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(expenses):
    amount = float(input("Enter the amount spent: "))
    description = input("Enter a brief description: ")
    category = input("Enter the category (e.g., food, transport): ")
    expense = {
        'amount': amount,
        'description': description,
        'category': category
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")

def show_expenses(expenses):
    if not expenses:
        print("No expenses recorded.")
        return
    for expense in expenses:
        print(f"Amount: ${expense['amount']:.2f}, Description: {expense['description']}, Category: {expense['category']}")

def analyze_expenses(expenses):
    from collections import defaultdict

    if not expenses:
        print("No expenses recorded.")
        return

    category_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    for expense in expenses:
        category_totals[expense['category']] += expense['amount']

        date = expense.get('date', '1970-01-01')[:7]
        monthly_totals[date] += expense['amount']

    print("\nCategory-wise Expenditure:")
    for category, total in category_totals.items():
        print(f"{category}: ${total:.2f}")

    print("\nMonthly Expenditure:")
    for month, total in monthly_totals.items():
        print(f"{month}: ${total:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            show_expenses(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
