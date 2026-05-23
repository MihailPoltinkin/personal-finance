def generate_report(transactions):
    total_income = sum(t[1] for t in transactions if t[0] == 'income')
    total_expense = sum(t[1] for t in transactions if t[0] == 'expense')
    return {'income': total_income, 'expense': total_expense, 'balance': total_income - total_expense}
