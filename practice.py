def main():
    printer()

def get_division(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

def printer():
    for number in range(1, 101):
        print(get_division(number))

main()
