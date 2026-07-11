def main():
    c = get_celsius("Celsius: ")
    print(round((c * 9/5)+ 32, 2))

def get_celsius(prompt):
    while True:
        try:
            return float(input(prompt)) 
        except ValueError:
            pass

main()