#create a custom function which runs the whole code
def main():
    weight = float(input("Enter the weight in kg. "))
    destination = input("Enter destination. (local or international) ").title()
    shipping_cost = get_shipping_cost(weight, destination)
    print(shipping_cost)
#create a function to calculate shipping cost
def get_shipping_cost(weight, destination):
    if destination !="Local" and destination !="International":
        return "invalid destination"
    elif weight<1 and destination=="Local":
        return "Shipping cost is $5"
    elif 1<=weight<=5 and destination == "Local":
        return "Shipping cost is $10"
    elif weight>5 and destination == "Local":
        return "Shipping cost is $20"

    elif weight<1 and destination=="International":
        return "Shipping cost is $15"
    elif 1<=weight<=5 and destination == "International":
        return "Shipping cost is $30"
    else:
        return "Shipping cost is $50"

#provide the user with the output using main
main()
