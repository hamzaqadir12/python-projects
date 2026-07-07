def main():
    number = get_number()
    printer(number)

# ask user for a positive number, keep asking until valid input is given
def get_number():
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n

# return FizzBuzz, Fizz, Buzz, or the number itself based on divisibility
def get_division(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# print the result for every number from 1 up to the given number
def printer(number):
    for count in range(1, number + 1):
        print(get_division(count))

main()
