def main():
    amt_due = 50
    #print(f"Amount due: {amt_due}")
    while amt_due > 0:
        print(f'Amount due: {amt_due}')
        amt_due = calculate_amt_due(amt_due)
    print(f'Change owed: {abs(amt_due)}')

def calculate_amt_due(amt_due):
    paid = int(input("Insert coin: "))
    if paid == 25:
        amt_due -= 25
    elif paid == 10:
        amt_due-=10
    elif paid == 5:
        amt_due-=5
    return amt_due