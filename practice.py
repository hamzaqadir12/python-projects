def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    if len(plate) < 2 or len(plate) > 6:
        return False
    if not plate[0].isalpha() or not plate[1].isalpha():
        return False
    for c in plate:
        if not c.isalnum():
            return False
    digit = False
    for c in plate:
        if c.isdigit():
            if not digit and c == "0":
                return False
            digit = True
        if c.isalpha() and digit:
            return False
    return True

main()