def game():
    coins = 0

    print("Choose an option: 0, 1, or 2 to earn that many coins. Reach 10 coins to win!\n")

    while coins < 10:
        try:
            choice = int(input("Enter your choice (0, 1, or 2): "))
            if choice not in [0, 1, 2]:
                print("Invalid choice. Please choose 0, 1, or 2.")
                continue
            coins += choice
            print(f"You earned {choice} coin(s). Total coins: {coins}\n")
        except ValueError:
            print("Enter a valid number (0, 1, or 2).")
    print("You've won the game")

def move_player(pos, direction):
    x, y = pos
    if direction == "up" and x > 0:
        x -= 1
    elif direction == "down" and x < 2:
        x += 1
    elif direction == "left" and y > 0:
        y -= 1
    elif direction == "right" and y < 2:
        y += 1
    else:
        print("Can't move in that direction!")
    return x, y

def display_grid(pos):
    for i in range(3):
        row = ""
        for j in range(3):
            if (i, j) == pos:
                row += "[P] "
            elif (i, j) == (1, 1):
                row += "[C] "
            elif (i, j) == (2, 2):
                row += "[S] "
            else:
                row += "[ ] "
        print(row)
    print("P=player, C=game")

    def shop(player):
        shop_items = {
            'potion': 2,
            'sword': 2,
            'sheild': 3
        }
        print('Welcome to the shop')
        print('Items for sale: ')
        for item, cost in shop_items.items():
            print(f" -{item.capitalize()}, {cost} coins")

        while True:
            print(f"\nCoins: {player['coins']}")
            inventory = ','.join(player['inventory']) or "Empty"
            print(f"Inventory: {inventory}")

            choice = input("Enter item to buy or 'exit' to leave: ").lower()

            if choice == 'exit':
                print("Leaving the shop.\n")
                break
            if choice not in shop_items:
                print("Item not found.")
                continue
            cost = shop_items[choice]
            if player["coins"] < cost:
                print("Not enough coins.")
            else:
                player["coins"] -= cost
                player["inventory"].append(choice)
                print(f"You bought a {choice}!")

def shop(player):
    shop_items={
        'potion':2,
        'sword':2,
        'sheild':3
    }
    print('Welcome to the shop')
    print('Items for sale: ')
    for item, cost in shop_items.items():
        print(f" -{item.capitalize()}, {cost} coins")

    while True:
        print(f"\nCoins: {player['coins']}")
        inventory= ','.join(player['inventory']) or "Empty"
        print(f"Inventory: {inventory}")

        choice = input("Enter item to buy or 'exit' to leave: ").lower()

        if choice == 'exit':
            print("Leaving the shop.\n")
            break
        if choice not in shop_items:
            print("Item not found.")
            continue
        cost = shop_items[choice]
        if player["coins"] < cost:
            print("Not enough coins.")
        else:
            player["coins"] -= cost
            player["inventory"].append(choice)
            print(f"You bought a {choice}!")

def main():
    player = {"coins": 0,
              "inventory": []
              }
    position = (0, 0)


    print("Move using: up, down, left, right. Type 'quit' to exit.\n")

    while player["coins"] < 10:
        display_grid(position)
        print(f"Current Coins: {player['coins']}")
        command = input("Enter move: ").lower()

        if command == "quit":
            print("Exiting the game.")
            break

        new_pos = move_player(position, command)
        if new_pos == position:
            continue
        position = new_pos

        if position == (1, 1):
            print("you're in the Coin Game!")
            play = input("Do you want to play the Game? (y/n): ").lower()
            if play == "y":
                game()

        elif position == (2,2):
            print("you are in the shop")
            shop(player)

if __name__ == "__main__":
    main()
