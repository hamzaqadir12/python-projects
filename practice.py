def main():
    x = get_num("X: ")
    opp =get_opp()
    while True:
        y = get_num("Y: ")
        try:
            print(round(get_calc(x, y, opp), 2))
            break
        except ZeroDivisionError:
            pass

def get_num(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass

def get_opp():
    while True:
        operator = input("Operator: ")
        if operator in ["+", "-", "*", "/"]:
            return operator

def get_calc(x, y, opp):
    if opp == "+":
        return x + y
    elif opp == "-":
        return x - y
    elif opp == "*":
        return x * y
    else:
        return x / y


main()