import random
def main():
    eat = get_option()
    choice = random.choice(eat)
    print(f"Tonight you eat at: {choice}")

def get_option():
    options = []
    while True:
        place = input("Place (or done): ")
        if place == "done":
            if options:
                break
            else:
                print("No options given")
        elif place.strip():
            options.append(place)
    return options

main()
