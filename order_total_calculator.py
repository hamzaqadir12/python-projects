#create a custom function of main
def main():
    price_per_item = float(input("What is the price per item? "))
    quantity = int(input(" Please enter the quantity. "))
    tax_rate = float(input(" What is the percentage of tax? "))
    subtotal = calculate_subtotal(price_per_item, quantity)
    total = calculate_total(subtotal, tax_rate)
    print(f"The total cost after tax is {total}")

#create a custom function of subtotal
def calculate_subtotal(price_per_item, quantity):
    return (price_per_item*quantity)

#create a custom function of total
def calculate_total(subtotal, tax_rate):
    return round(subtotal+((subtotal*tax_rate)/100),2)
#provide the user with the output
main()
