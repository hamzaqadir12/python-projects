def main():
    a, b, c, d, f = total(get_student_number())
    printer(a, b, c, d, f)

# ask for a positive number of students, keep asking until valid input is given
def get_student_number():
    while True:
        n = int(input("Number of students:  "))
        if n > 0:
            return n
        
# return the letter grade for a given score
def category(scores):
    if 90 <= scores <=100:
        return "A"
    elif 80 <= scores < 90:
        return "B"
    elif 70 <= scores < 80:
        return "C"
    elif 60 <= scores < 70:
        return "D"
    else:
        return "F"
    
# collect scores for each student and count how many fall into each grade category
def total(student_count):
    A = B = C = D = F = 0
    for _ in range(student_count):
        while True:
            score = int(input("Score: "))
            if 0 <= score <= 100:
                break
        grade = category(score)
        if grade == "A":
            A += 1
        elif grade == "B":
            B += 1
        elif grade == "C":
            C += 1
        elif grade == "D":
            D += 1
        else:
            F += 1
    return A, B, C, D, F

# display the total count of students in each grade category
def printer(a, b, c, d, f):
    print(f"A: {a}")
    print(f"B: {b}")
    print(f"C: {c}")
    print(f"D: {d}")
    print(f"F: {f}")

main()
