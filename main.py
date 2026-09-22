import json, os, sys
from utils import add_expense, view_all_expenses, view_by_category, delete_expense

if os.path.exists('transactions.json'):
    with open('transactions.json', 'r') as file:
        transactions = json.load(file)
else:
    transactions = []

while True:
    print('\n==== Expense Tracker ====')
    print('(1) Add expense | (2) View all | (3) View by category | (4) Delete expense | (5) Exit')
    user_input = input('> ').strip()

    if user_input == '1':
        add_expense(transactions)

        with open('transactions.json', 'w') as file:
            json.dump(transactions, file, indent=4)
    elif user_input == '2':
        view_all_expenses(transactions)
    elif user_input == '3':
        view_by_category(transactions)
    elif user_input == '4':
        delete_expense(transactions)
    elif user_input == '5':
        sys.exit()
    else:
        print('Please enter a valid option')