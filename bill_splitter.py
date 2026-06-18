#ask the total bill amount< tip percentage, and people
total_bill = float(input("What is the total amount of the bill? "))
total_bill = round(total_bill, 2)
tip_percentage = float(input("What is the percentage of tip? "))
tip_percentage = round(tip_percentage, 2)
people = int(input("How many people are splitting the bill? "))
#calculate the tip amount, bill after tip, and per head
tip_amount = total_bill*(tip_percentage/100)
tip_amount = round(tip_amount, 2)
bill_after_tip = total_bill+tip_amount
bill_after_tip = round(bill_after_tip, 2)
per_person = (bill_after_tip/people)
per_person = round(per_person, 2)
#provide the user with all the information
print(f"Tip amount:${tip_amount}")
print(f"Total bill with tip:${bill_after_tip}")
print(f"Each person pays:${per_person}")
