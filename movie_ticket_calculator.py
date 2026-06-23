# create a custom function of main
def main():
    age = int(input("What's your age? "))
    quantity = int(input("How many tickets are required? "))
    price = get_ticket_price(age)
    total = calculate_total(price, quantity)
    print(f"The total for the tickets are ${total}")

#create a function to match the age with the ticket price
def get_ticket_price(age):
    if age < 12:
        return 5
    elif 12<=age<=17:
        return 8
    elif 18<=age<=64:
        return 12
    else:
        return 7

#create a function to calculate the total
def calculate_total(price, quantity):
    return round(price * quantity,2)

#provide the user with the output
main()
