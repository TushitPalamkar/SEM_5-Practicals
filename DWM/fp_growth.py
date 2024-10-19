import pyfpgrowth
def get_transactions():
    transactions=[]
    num=int(input("Enter the no of transactions:"))
    for i in range(num):
        items=input(f"Enter the items for transaction {i+1}:").split(',')
        transactions.append([item.strip() for item in items if item.strip()])
        
    return transactions
transactions=get_transactions()
# transactions=[['milk','bread','butter'],['bread','butter'],['milk','eggs'],['bread','milk','butter'],['eggs','bread']]
patterns=pyfpgrowth.find_frequent_patterns(transactions,2)
rules=pyfpgrowth.generate_association_rules(patterns,0.7)
print(f"Frequent patterns:{patterns}")
print(f"Rules:{rules}")