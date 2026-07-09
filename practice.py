def main():
    number = get_number()
    printer(number)

def get_number():
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n

def printer(number):
    # top half
    for row in range(1, number + 1):
        print(" " * (number - row) + "#" * (2 * row - 1))
    
    # bottom half
    for row in range(1, number):
        print(" " * row + "#" * (2 * (number - row) - 1))

main()
