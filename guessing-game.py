def main():
    print("Python Guessing Game")
    print("====================\n")
    ans = "zebra"
    while True:
        print("I'm thinking of an animal.\n")
        guess = input("Enter the name of an animal: ").strip().lower()
        if guess == ans:
            print("\nCongratulations, you win!")
            feedback = input("\nDo you like this animal? Enter 'y' or 'n': ").strip().lower()
            if feedback == "y":
                print("\nI'm glad. Thank you for playing!")
            elif feedback == "n":
                print("\nI'm sorry you feel that way. Thank you for playing!")
            break
        elif guess[0] == "q" : 
            print("\nThank you for playing!")
            break
        else:
            print("\nSorry, try again.\n")
main()

    
