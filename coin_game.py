def game():
    coins = 0
    print("Choose an option: 0, 1, or 2 to earn that many coins. Reach 100 coins to win!\n")

    while coins < 100:
        try:
            choice = int(input("Enter your choice (0, 1, or 2): "))
            if choice not in [0, 1, 2]:
                print("Invalid choice. Please choose 0, 1, or 2.")
                continue
            coins += choice
            print(f"You earned {choice} coin(s). Total coins: {coins}\n")
        except ValueError:
            print("Please enter a valid number (0, 1, or 2).")

    print("Congratulations! You reached 100 coins and won the game!")


game()
