def main():
    a = get_age("Age: ")
    print(f"Valid age: {a}")

def get_age(prompt):
    while True:
        try:
            age = int(input(prompt))
            if 0 <= age <= 120:
                return age
            else:
                print("Invalid age")
        except ValueError:
            print("Invalid age")

main()