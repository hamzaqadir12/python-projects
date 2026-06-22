def main():
    length = float(input("What is the length of the wall? "))
    width = float(input("What is the width of the wall? "))
    coverage_rate = float(input("What is the paint's coverage rate in square meter per liter? "))
    area = calculate_area(length, width)
    paint_needed = calculate_paint_needed(area, coverage_rate)
    print(f"{paint_needed} liters of paint is required. ")

#create a custom function of area
def calculate_area(length, width):
    return length*width

#create a custom function of paint needed
def calculate_paint_needed(area, coverage_rate):
    return round(area/coverage_rate, 2)

#provide the user with the output
main()
