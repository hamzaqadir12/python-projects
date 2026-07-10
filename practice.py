def main():
    f = get_float("F: ")
    print(f)

def get_float(prompt):
    while True:
        try:
            return round(float(input(prompt)),2)
        except ValueError:
            pass

main()