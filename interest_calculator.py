#create a custom function
def calculate_interest(principal, rate, time):
    return round((principal*rate*time)/100,2)
#ask the user to input values
print("Enter values in form of numbers. ")
principal = float(input("Enter the principal amount "))
rate = float(input("Enter the percentage rate "))
time = float(input("Enter the total time "))
#provide the user with the output
print(f"The amount of interest is {calculate_interest(principal, rate, time)}")
