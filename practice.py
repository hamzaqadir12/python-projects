def main():
    number = get_number()
    printer(number)

# ask user for a positive number, keep asking until valid input is given
def get_number():
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n

def printer(number):
    for _ in range(number):
        print("#" * number)

main()
