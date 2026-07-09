def main():
    x = get_number()
    print(f"X is {x}")

def get_number():
    while True:
        try:
            x = int(input("X: "))
            if 0 <= x <=100:
                return x
        except ValueError:
            print("Enter an integer")

main()