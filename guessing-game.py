def main():
    print("Python Guessing Game")
    print("====================\n")
    ans = "zebra"
    while True:
        print("I'm thinking of an animal.\n")
        guess = input("Enter the name of an animal: ").strip().lower()
        if guess == ans:
            print("\nCongratulations, you win!")
            break
        elif guess == "quit":
            print("\nThank you for playing!")
            break
        else:
            print("\nSorry, try again.\n")
main()

    
