def main():
    string = input("String: ")
    count = get_count("Count: ")
    print(string * count)

def get_count(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value 
        except ValueError:
            pass

main()