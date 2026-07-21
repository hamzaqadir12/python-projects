def main():
    change = get_calc()
    print(f"Change Owed: {change}")

def get_calc():
    amount_due = 50
    while True:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))
        if coin in [5, 10, 25]:
            amount_due = amount_due - coin
        if amount_due <= 0:
            return abs(amount_due)

main()
