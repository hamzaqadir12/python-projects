def main():
    x = get_number()
    print(f"X is {x}")

def get_number():
    while True:
        try:
            return int(input("X: "))
        except ValueError:
            pass

main()