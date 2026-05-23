def analyze_categories(transactions):
    categories = {}
    for trans_type, amount in transactions:
        if trans_type not in categories:
            categories[trans_type] = 0
        categories[trans_type] += amount
    return categories

def get_top_category(transactions):
    categories = analyze_categories(transactions)
    if not categories:
        return None
    return max(categories, key=categories.get)
