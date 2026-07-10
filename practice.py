def main():
    x = get_number("X: ")
    y = get_number("Y: ")
    print(f"X is {x} and Y is {y}")

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()