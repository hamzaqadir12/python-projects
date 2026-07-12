def main():
    w = get_word()
    if w == w[::-1]:
        print("Palindrome")
    else:
        print("Not a palindrome")

def get_word():
    while True:
        word = input("Word: ").lower()
        if word.strip():
            return word
    
main()