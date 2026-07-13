def main():
    n = get_num("Number: ")
    print(f"Your number is {n}")

def get_num(prompt):
    while True:
        try:
            number = int(input(prompt))
            if number > 0:
                return number
        except ValueError:
            print("Not an integer")
        else:
            print("Too small")

main()