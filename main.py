# main.py
balance = 0
transactions = []

def add_income(amount):
    global balance
    balance += amount
    transactions.append(('income', amount))

def add_expense(amount):
    global balance
    balance -= amount
    transactions.append(('expense', amount))