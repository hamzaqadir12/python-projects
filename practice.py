def main():
    x = get_int("X: ")
    y = get_int("Y: ")
    opp = get_opp("Operator: ")
    while True:
        try:
            answer = get_calc(x, y, opp)
            print(round(float(answer),2))
            break
        except ZeroDivisionError:
            y = get_int("Y: ")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))

        except ValueError:
            pass

def get_opp(prompt):
    while True:
        operator = input(prompt)
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
