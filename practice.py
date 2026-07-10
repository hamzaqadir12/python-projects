def main():
    x = get_int("X: ")
    while True:
        y = get_int("Y: ")
        try:
            print(x / y)
            break
        except ZeroDivisionError:
            pass

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()