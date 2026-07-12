def main():
    sent = get_sentence()
    print(len(sent.split()))

def get_sentence():
    while True:
        sent = input("Sentence: ")
        if len(sent.split()) == 0:
            print("Invalid input")
        else:
            return sent

main()