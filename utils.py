import json

ID_WIDTH = 5
CATEGORY_WIDTH = 15
DESCRIPTION_WIDTH = 20
AMOUNT_WIDTH = 12

def add_expense(transactions):
    while True:
        try:
            amount = int(input('Specify amount: '))
            if amount == 0 or amount < 0:
                print('Amount must be positive')
                continue
            break
        except ValueError:
            print('Please enter a number\n')

    category = input('Specify category: ')
    description = input('Add description: ')

    if transactions:
        transaction_id = transactions[-1]['id'] + 1
    else:
        transaction_id = 1

    expense = {
        'id': transaction_id,
        'amount': amount,
        'category': category,
        'description': description,
    }

    transactions.append(expense)
    print('Expense added successfully.')

def view_all_expenses(transactions):
    if not transactions:
        print('Transactions list is empty')
        return

    print(f"{'ID':<{ID_WIDTH}} {'Category':<{CATEGORY_WIDTH}} {'Description':<{DESCRIPTION_WIDTH}} {'Amount':>{AMOUNT_WIDTH}}")

    for t in transactions:
        Id = t['id']
        category = t['category']
        description = t['description']
        amount = t['amount']
        print(f"{Id:<{ID_WIDTH}} {category:<{CATEGORY_WIDTH}} {description:<{DESCRIPTION_WIDTH}} {amount:>{AMOUNT_WIDTH},}")

    total_spending = sum(t['amount'] for t in transactions)
    
    print(f'\nTotal Spending is {total_spending}')

def view_by_category(transactions):
    if not transactions:
        print('Transactions list is empty')
        return
    
    spending = {}

    for t in transactions:
        category = t['category']
        amount = t['amount']

        if category in spending:
            spending[category] += amount
        else:
            spending[category] = amount

    print(f"\n{'Category':<{CATEGORY_WIDTH}} {'Total Spending':>{AMOUNT_WIDTH}}")        
    for category, amount in spending.items():
        print(f"{category:<{CATEGORY_WIDTH}} {amount:>{AMOUNT_WIDTH},}")

def delete_expense(transactions):
    if transactions:
        print(f"{'ID':<{ID_WIDTH}} {'Category':<{CATEGORY_WIDTH}} {'Description':<{DESCRIPTION_WIDTH}} {'Amount':>{AMOUNT_WIDTH},}")

        for t in transactions:
                Id = t['id']
                category = t['category']
                description = t['description']
                amount = t['amount']
                print(f"{Id:<{ID_WIDTH}} {category:<{CATEGORY_WIDTH}} {description:<{DESCRIPTION_WIDTH}} {amount:>{AMOUNT_WIDTH},}")
    else:
        print('Transactions list is empty (nothing to delete)')
        return
    while True:
        try:
            delete_id = int(input('Enter transaction ID: '))
            break
        except ValueError:
            print('Please enter a number\n')

    for t in transactions:
        if t['id'] == delete_id:
            transactions.remove(t)
            break
    else:
        print('Transaction does not exist')
        return
    
    with open('transactions.json', 'w') as file:
        json.dump(transactions, file, indent=4)

    print('Transaction deleted')