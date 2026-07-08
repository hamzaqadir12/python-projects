def main():
    number = get_number()
    printer(number)

def get_number():
    while True:
        n = int(input("Number: "))
        if n > 0:
            return n

def printer(number):
    for row in range(1, number + 1):
        for column in range(1, number + 1):
            print(row, end=" ")
        print()
main()
