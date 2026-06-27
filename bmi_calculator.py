#create a custom function which runs the whole code
def main():
    weight = float(input("Enter weight in kg. " ))
    height = float(input("Enter height in meters. "))
    bmi = calculate_bmi(weight, height)
    category = get_category(bmi)
    print(f"Your BMI is {bmi}. {category}")

#create a custom function which calculates bmi
def calculate_bmi(weight, height):
    return round(weight/(height**2),1)

#create a custom function which assigns the bmi to a category
def get_category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<=24.9:
        return "Normal weight"
    elif 25<=bmi<=29.9:
        return "Overweight"
    else:
        return "Obese"

#provide the user with the output
main()
